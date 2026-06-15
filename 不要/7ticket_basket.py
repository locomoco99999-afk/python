import re
import requests
import os
from datetime import datetime, date
from bs4 import BeautifulSoup
import json
janru="g/000428"
BASE_URL = "https://7ticket.jp/"
TARGET_URL = BASE_URL + janru

folder_path = "C:/python/7ticket/endcnt"
os.makedirs(folder_path, exist_ok=True)

#janru_cnt=janru.replace("/", "-")+"txt"
filepath_cnt = f"{folder_path}/endcnt_7basket.txt"
filepath='C:/python/7ticket/7basket.txt'


now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
sabun_txt='C:/python/7ticket/'+now_str+'_sabun_basket.txt'


before_filename=""
before_filepath=""

add_filename=""
add_filepath=""
delete_filename=""
delete_filepath=""

# ファイルが存在しているかチェック
if os.path.exists(filepath):
  
    # ディレクトリとファイル名を分離
    directory, filename = os.path.split(filepath)

    # 新しいファイル名を作成
    before_filename = f"{now_str}_{filename}"
    before_filepath = os.path.join(directory, before_filename)

    add_filename = f"add_{filename}"
    add_filepath = os.path.join(directory, before_filename)

    delete_filename = f"delete_{filename}"
    delete_filepath = os.path.join(directory, before_filename)

    # リネーム
    os.rename(filepath, before_filepath)
    print(f"既存ファイルをリネームしました → {before_filepath}")
else:
    print("既存ファイルはありません。")



#出力データ
data=""



team_lists = [
    ["レバンガ北海道", "g/001127"],
    ["茨城ロボッツ", "g/000747"],
    ["滋賀レイクス", "g/002144"],
    ["青森ワッツ", "g/001933"],
    ["福島ファイヤーボンズ", "g/001937"],
    ["信州ブレイブウォリアーズ", "g/000695"],
    ["バンビシャス奈良", "g/001930"],
    ["ライジングゼファーフクオカ", "g/000690"],
    ["東京八王子ビートレインズ", "g/000891"],
    ["新潟アルビレックスBB", "g/000687"],
    ["金沢武士団", "g/000709"],
    ["岐阜スゥープス", "g/001608"],
    ["香川ファイブアローズ", "g/000688"]
]

janru=janru.replace('/', '-')



#出力データ
data=""

eventName=""
team=""
seat_name=""
kaijo=""
kouenbi=""
kaien_jikan=""
iconStr=""
typeStr=""
priceStr=""
kobetu_url=""
for teams in team_lists:
    teamName=teams[0]
    team_url=teams[1]




    TARGET_URL = BASE_URL + team_url
    print(TARGET_URL)

    print(eventName)

    #ページ取得
    response = requests.get(TARGET_URL)


    #タグを整形
    soup = BeautifulSoup(response.content, "html.parser")

    #aタグ取得
    links = soup.find_all("a")

    #リスト
    eventList = []

    #リンクを繰り返し
    for link in links:

        #開催日のリンクを指定
        href = link.get("href")
        if href and ("cal" in href or "/s/" in href):
            if href.startswith("/"):
                href = BASE_URL + href
            
            print(href)
            eventList.append(href)
    
    #イベント件数取得
    eventKensu=len(eventList)
    print(eventKensu)


    #座席一覧繰り返し
    for i in range(eventKensu):
    #   print(eventList[i])

        #1つずつイベント指定
        eventUrl=eventList[i]
        # print(eventUrl)

        print(eventList[i])



        #ページ取得
        eventResp = requests.get(eventUrl, timeout=(3.0, 7.5))
        eventsoup = BeautifulSoup(eventResp.content, "html.parser")

        scheduleTable=eventsoup.find('table', attrs={ 'class': ['scheduleTable'] } )
        #この形式だったらクリックして遷移する
        #12/27（土）	 ×14:05
        #12/28（日）	 ×14:05

        if scheduleTable is not None:

            # aタグ全部取得
            detail_links = scheduleTable.find_all('a')

            for a in detail_links:
                href = BASE_URL+a.get('href')
                print(href)

                eventDetailResp = requests.get(href, timeout=(3.0, 7.5))
                eventDetailsoup = BeautifulSoup(eventDetailResp.content, "html.parser")
                eventName_detail=eventDetailsoup.find('p', attrs={ 'class': ['eventName'] } ).text

                eventName_detail=eventDetailsoup.find('p', attrs={ 'class': ['eventName'] } ).text

                print(eventName_detail)


                items = eventDetailsoup.select("dl.eventInfo dt, dl.eventInfo dd")

                # 2) ペアにして辞書化
                event_info = {}
                for i in range(0, len(items), 2):
                    key = items[i].get_text(strip=True)
                    value = items[i+1].get_text(strip=True)
                    event_info[key] = value

                # 結果
                kaijo = event_info.get("会場", "")
                kouenbi=event_info.get("公演日", "") 
            
                kouenbi_text = kouenbi.strip()  # 念のため
                # ① 日付部分だけ抽出（例: 2026/01/18）
                m = re.search(r"\d{4}/\d{2}/\d{2}", kouenbi_text)
                if m:
                    date_str = m.group()
                    kaisai_date = datetime.strptime(date_str, "%Y/%m/%d").date()
                    today = date.today()

                    # 2日後以前なら continue
                    if (kaisai_date - today).days <= 2:
                        print("開催日が2日後以前のため飛ばす"+kouenbi_text)
                        continue
                else:
                    print("日付が抽出できません:", kouenbi)
                    continue    

                
        


                kaien_jikan = event_info.get("開演時間", "")
                

                eventName=eventDetailsoup.find('p', attrs={ 'class': ['eventName'] } ).text

                hidukelist=eventDetailsoup.find_all('th', attrs={ 'class': ['seatType'] } )

                    #1チケットずつ処理したいので行単位で取得する
                #data=data+eventUrl+"\n"
                for row in hidukelist:


                    icon=row.select_one('.icon')
                    iconStr=icon.getText()
                    

                    type=row.select_one('.type')
                    typeStr=type.getText()

                    price=row.select_one('.price')
                    priceStr=price.getText().replace(' ', '').replace('\n', '')


                    text=teamName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl+"///"+eventName

                    if "○" in iconStr and "×" not in iconStr:
                        print(text)
                        data=data+text+"\n"
                  
        else:
            eventName_detail=eventsoup.find('p', attrs={ 'class': ['eventName'] } ).text

            print(eventName)

    
            table = eventsoup.select_one("table.scheduleTable.mgb05")

            detailtsoup = BeautifulSoup(eventResp.content, "html.parser")

            items = detailtsoup.select("dl.eventInfo dt, dl.eventInfo dd")

            # 2) ペアにして辞書化
            event_info = {}
            for i in range(0, len(items), 2):
                key = items[i].get_text(strip=True)
                value = items[i+1].get_text(strip=True)
                event_info[key] = value

            # 結果
            kaijo = event_info.get("会場", "")
            kouenbi=event_info.get("公演日", "") 
            
            kouenbi_text = kouenbi.strip()  # 念のため
            # ① 日付部分だけ抽出（例: 2026/01/18）
            m = re.search(r"\d{4}/\d{2}/\d{2}", kouenbi_text)
            if m:
                date_str = m.group()
                kaisai_date = datetime.strptime(date_str, "%Y/%m/%d").date()
                today = date.today()

                # 2日後以前なら continue
                if (kaisai_date - today).days <= 2:
                    print("開催日が2日後以前のため飛ばす"+kouenbi_text)
                    continue
            else:
                print("日付が抽出できません:", kouenbi)
                continue    

            
    


            kaien_jikan = event_info.get("開演時間", "")
            

            eventName=eventsoup.find('p', attrs={ 'class': ['eventName'] } ).text

            hidukelist=eventsoup.find_all('th', attrs={ 'class': ['seatType'] } )

                #1チケットずつ処理したいので行単位で取得する
            #data=data+eventUrl+"\n"
            for row in hidukelist:


                icon=row.select_one('.icon')
                iconStr=icon.getText()
                

                type=row.select_one('.type')
                typeStr=type.getText()

                price=row.select_one('.price')
                priceStr=price.getText().replace(' ', '').replace('\n', '')


                text=teamName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl+"///"+eventName

                if "○" in iconStr and "×" not in iconStr:
                    print(text)
                    data=data+text+"\n"
                 



# ファイルを開く
with open(filepath, 'w+',encoding='UTF-8') as file:

    # 文字列をファイルに書き込む
    file.write(data)
    file.close
    

with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
    # 文字列をファイルに書き込む
    file.write(str(0))
    file.close



print("処理終了 差分比較処理開始")



# ファイルの行を読み込んでセット化（重複なし）
with open(before_filepath, "r", encoding="utf-8") as f:
    before_lines = set(f.read().splitlines())

with open(filepath, "r", encoding="utf-8") as f:
    after_lines = set(f.read().splitlines())

# 差分を計算
only_in_before = before_lines - after_lines     # before にだけある
only_in_after = after_lines - before_lines      # after にだけある

# sabun_txt に書き込む
with open(sabun_txt, "w", encoding="utf-8") as f:
    if only_in_before:
        f.write("▼ 削除されたもの\n")
        for line in sorted(only_in_before):
            f.write(line + "\n")

    if only_in_after:
        f.write("\n▼ 追加になったもの\n")
        for line in sorted(only_in_after):
            f.write(line + "\n")

print("差分を sabun_txt に書き込みました。")



# ファイルの行を読み込んでセット化（重複なし）
with open(before_filepath, "r", encoding="utf-8") as f:
    before_lines = set(f.read().splitlines())

with open(filepath, "r", encoding="utf-8") as f:
    after_lines = set(f.read().splitlines())

# 差分を計算
only_in_after = after_lines - before_lines      # 追加された行
only_in_before = before_lines - after_lines     # 削除された行

# 追加された行を書き込む
with open(add_filepath, "w", encoding="utf-8") as f:
    for line in sorted(only_in_after):
        f.write(line + "\n")

# 削除された行を書き込む
with open(delete_filepath, "w", encoding="utf-8") as f:
    for line in sorted(only_in_before):
        f.write(line + "\n")

print("追加行 → add_filepath に書き込み完了")
print("削除行 → delete_filepath に書き込み完了")