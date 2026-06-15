import re
import requests
import os
from datetime import datetime, date
from bs4 import BeautifulSoup

janru="g/000428"
BASE_URL = "https://7ticket.jp/"
TARGET_URL = BASE_URL + janru

folder_path = "C:/python/7ticket/endcnt"
os.makedirs(folder_path, exist_ok=True)

#janru_cnt=janru.replace("/", "-")+"txt"
filepath_cnt = f"{folder_path}/endcnt_7artist.txt"


#出力データ
data=""




#ページ取得
response = requests.get(TARGET_URL)


janru=janru.replace('/', '-')
filepath='C:/python/7ticket/7artist.txt'


#タグを整形
soup = BeautifulSoup(response.content, "html.parser")

#aタグ取得
links = soup.find_all("a")

#リスト
eventList = []

with open(r"C:\python\artistlist.txt", "r", encoding="utf-8") as f:
    artist_list = [line.strip() for line in f if line.strip()]


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



    eventName=eventsoup.find('p', attrs={ 'class': ['eventName'] } ).text

    print(eventName)


    if not any(a.lower() in eventName.lower() for a in artist_list):
        print("アーティストのリストに無いから次へ"+eventName)
        continue


 
    table = eventsoup.select_one("table.scheduleTable.mgb05")


    if table:
        # href をすべて取得
        links = [a["href"] for a in table.select("a[href]")]
        
        print("取得したリンク一覧:")
        for link in links:
            print(link)
        
        # 順にリンク先を開く（例: 実際に遷移するなら）
       
        for href in links:
            full_url = href if href.startswith("http") else BASE_URL + href
            print(f"アクセス中: {full_url}")
            detailResp = requests.get(full_url)
            if detailResp.ok:
                print(f"→ {full_url} にアクセス成功 ({len(detailResp.text)} bytes)")
                detailtsoup = BeautifulSoup(detailResp.content, "html.parser")

                items = detailtsoup.select("dl.eventInfo dt, dl.eventInfo dd")

                 # 2) ペアにして辞書化
                event_info = {}
                for i in range(0, len(items), 2):
                    key = items[i].get_text(strip=True)
                    value = items[i+1].get_text(strip=True)
                    event_info[key] = value

                # 結果
                kaijo = event_info.get("会場", "")
                kouenbi = event_info.get("公演日", "")

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


                    text=eventName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl

                    if "○" in iconStr and "×" not in iconStr:
                        print(text)
                        data=data+text+"\n"


                    else:
                        print(f"→ {full_url} にアクセス失敗 ({detailResp.status_code})")
                



    else:

    # 1) 全ての dt と dd を順番通りに取得
        items = eventsoup.select("dl.eventInfo dt, dl.eventInfo dd")
        # 2) ペアにして辞書化
        event_info = {}
        for i in range(0, len(items), 2):
            key = items[i].get_text(strip=True)
            value = items[i+1].get_text(strip=True)
            event_info[key] = value

        # 結果
        kaijo = event_info.get("会場", "")
        kouenbi = event_info.get("公演日", "")
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


            text=eventName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl

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


print("処理終了")
