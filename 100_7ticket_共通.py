import subprocess

import re
import requests
import os
from datetime import datetime, date
from bs4 import BeautifulSoup
import json
import re
import unicodedata



BASE_URL = "https://7ticket.jp/"

eventKbn = input("7チケット　共通 処理を選択してください:1=木下大サーカス立川,2=ポップサーカス,3=ハッピードリームサーカス,4=バスケット,5=野球,6=アーティスト,7=木下大サーカス磐田,8=木下大サーカス岡山")
if eventKbn=="1" :
    janru="s/111899/d"
    eventNameTittle="木下大サーカス"
    baseFolder="7ticket"
elif eventKbn=="2":
    janru="s/112283/d"
    eventNameTittle="ポップサーカス"
    baseFolder="7ticket"
elif eventKbn=="3":
    janru="s/112858/d"
    eventNameTittle="ハッピードリームサーカス"
    baseFolder="7ticket"
elif eventKbn=="4":
    janru="s/000428"
    eventNameTittle="バスケット"
    baseFolder="7ticket"
elif eventKbn=="5":
    janru="s/000001"
    eventNameTittle="野球"
    baseFolder="7ticket"
elif eventKbn=="6":
    subprocess.run(["python", "104_アーティスト.py"])
elif eventKbn=="7" :
    janru="s/113193/d"
    eventNameTittle="木下大サーカス_磐田"
    baseFolder="7ticket"
elif eventKbn=="8" :
    janru="s/115673/d"
    eventNameTittle="木下大サーカス_岡山"
    baseFolder="7ticket"

else :
    print("その他の入力、終了します。")
    quit()

eventName_txt=eventNameTittle

if eventKbn=="7" :
    eventName_txt="木下大サーカス"


folder_path_moto= "C:/python/7ticket/"+eventNameTittle
filepath='C:/python/7ticket/'+eventNameTittle+'/7ticket_'+eventNameTittle+'.txt'
folder_path = "C:/python/7ticket/"+eventNameTittle+"/endcnt"
configfile=folder_path_moto+"/設定/設定ファイル.txt"
configfile_team=folder_path_moto+"/設定/設定_チームリスト.txt"
configfile_team_eigo=folder_path_moto+"/設定/設定_チーム英語リスト.txt"
configfile_ng=folder_path_moto+"/設定/設定_NG席リスト.txt"
configfile_seat=folder_path_moto+"/設定/設定_座席リスト.txt"

os.makedirs(folder_path, exist_ok=True)
filepath_cnt = f"{folder_path}/endcnt_7ticket_"+eventNameTittle+".txt"

# 現在時刻を YYYYMMDD_HHMMSS の形式で取得
now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
sabun_txt=folder_path_moto+'/差分_'+now_str+'_'+eventNameTittle+'.txt'


with open(configfile, "r", encoding="utf-8-sig") as f:
    config = json.load(f)

chokusetukeisai= config["直接掲載"]
daycount = config["掲載日数"]



with open(configfile_team, "r", encoding="utf-8-sig") as f:
    config_team = json.load(f)
team_lists = config_team["team_lists"]

with open(configfile_team_eigo, "r", encoding="utf-8-sig") as f:
    config_team_eigo = json.load(f)
team_eigo_dict = config_team_eigo["team_eigo_dict"]

with open(configfile_ng, "r", encoding="utf-8-sig") as f:
     config_ng = json.load(f)
ngwords = config_ng["ngwords"]

with open(configfile_seat, "r", encoding="utf-8") as f:
    config_seat = json.load(f)
seat_map = config_seat["seat_map"]

#出力データ
data=""

eventName=eventNameTittle



if team_lists :
    print("team_listsが空じゃない！！")

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

        eventKensu=0
        #日付指定なしで直接席が表示されるパターン
        if eventKbn=="6":
          
           
            for link in links:
                href = link.get("href")
                if href and ("cal" in href or "/s/" in href):
                    if href.startswith("/"):
                        href = BASE_URL + href
                        eventList.append(href)

                        eventKensu=len(eventList)
                        print(eventKensu)

            if eventKensu== 0:
                eventList.append(TARGET_URL)
                eventKensu=1
        else :
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
                    kouenbi_text = kouenbi_text.replace(" ", "")
                    kouenbi_text = re.sub(r"\s+", "", kouenbi_text)   
                    kouenbi_text = unicodedata.normalize("NFKC", kouenbi_text)

                    # 空白（半角・全角・不可視）を削除
                    kouenbi_text = re.sub(r"[\s\u200b\u00a0]", "", kouenbi_text)

                    # 日本語の曜日を削除（（日）（月）など）
                    kouenbi_text = re.sub(r"[（(][日月火水木金土][）)]", "", kouenbi_text)                    

                    print("check:"+repr(kouenbi_text))
                    # ① 日付部分だけ抽出（例: 2026/01/18）
                    m = re.search(r"(\d{4})\D+(\d{1,2})\D+(\d{1,2})", kouenbi_text)
                    if m:
                        date_str = m.group()
                        kaisai_date = datetime.strptime(date_str, "%Y/%m/%d").date()
                        today = date.today()

                        # daycount日後以前なら continue
                        if (kaisai_date - today).days <= daycount:
                            print("開催日がdaycount日後以前のため飛ばす"+kouenbi_text)
                            continue
                    else:
                        print("日付が抽出できません:", kouenbi_text)
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

                detailtsoup = BeautifulSoup(eventResp.content, "html.parser")

                items = detailtsoup.select("dl.eventInfo dt, dl.eventInfo dd")

                # 要素が取れなかった場合
                if not items:
                    print("eventInfo が見つからないのでリンクをクリックして遷移します")

                    evlinks = detailtsoup.select("ul.resultList li a")

                    for evlink in evlinks:
                        text = evlink.text.strip()

                        # 駐車場は除外
                        if "駐車券" in text and "一般販売" not in text:
                            continue

                        href = evlink.get("href")
                        if href == "/inquiry":
                            continue

                        if href:
                            target_url_ = BASE_URL + href
                            print("遷移先:", target_url_)
                                # /inquiry を除外
 
                            # 遷移
                            if target_url_:
                                            eventResp = requests.get(target_url_, timeout=(3.0, 7.5))
                                            eventsoup = BeautifulSoup(eventResp.content, "html.parser")
                                            response = requests.get(target_url_)
                            break




                try:
                    eventName_detail=eventsoup.find('p', attrs={ 'class': ['eventName'] } ).text
                except Exception:
                    continue
               
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
                kouenbi_text = kouenbi_text.replace(" ", "")
                kouenbi_text = re.sub(r"\s+", "", kouenbi_text)   
                kouenbi_text = unicodedata.normalize("NFKC", kouenbi_text)

                # 空白（半角・全角・不可視）を削除
                kouenbi_text = re.sub(r"[\s\u200b\u00a0]", "", kouenbi_text)

                # 日本語の曜日を削除（（日）（月）など）
                kouenbi_text = re.sub(r"[（(][日月火水木金土][）)]", "", kouenbi_text)

                # ① 日付部分だけ抽出（例: 2026/01/18）
                print("check:"+repr(kouenbi_text))
                m = re.search(r"(\d{4})\D+(\d{1,2})\D+(\d{1,2})", kouenbi_text)
                if m:
                    date_str = m.group()
                    kaisai_date = datetime.strptime(date_str, "%Y/%m/%d").date()
                    today = date.today()

                    # 2日後以前なら continue
                    if (kaisai_date - today).days <= daycount:
                        print("開催日がdaycount日後以前のため飛ばす"+kouenbi_text)
                        continue
                else:
                    print("日付が抽出できません:", kouenbi_text)
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

else : #team_listが空なので直接そのサイト内を処理する
    TARGET_URL = BASE_URL + janru
        
    print(TARGET_URL)


    #ページ取得
    response = requests.get(TARGET_URL)


    #タグを整形
    soup = BeautifulSoup(response.content, "html.parser")

    #aタグ取得
    links = soup.find_all("a")

    #リスト
    eventList = []



    #today = datetime.now().strftime("%Y%m%d")






    before_filename=""
    before_filepath=""

    add_filename=""
    add_filepath=""
    delete_filename=""
    delete_filepath=""



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
        eventResp = requests.get(eventUrl, timeout=(10, 20))
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
                kouenbi_text = kouenbi_text.replace(" ", "")                
                kouenbi_text = re.sub(r"\s+", "", kouenbi_text)       
                kouenbi_text = unicodedata.normalize("NFKC", kouenbi_text)

                # 空白（半角・全角・不可視）を削除
                kouenbi_text = re.sub(r"[\s\u200b\u00a0]", "", kouenbi_text)

                # 日本語の曜日を削除（（日）（月）など）
                kouenbi_text = re.sub(r"[（(][日月火水木金土][）)]", "", kouenbi_text)


                # ① 日付部分だけ抽出（例: 2026/01/18）
                print("check:"+repr(kouenbi_text))
                m = re.search(r"(\d{4})\D+(\d{1,2})\D+(\d{1,2})", kouenbi_text)
                if m:
                    date_str = m.group()
                    kaisai_date = datetime.strptime(date_str, "%Y/%m/%d").date()
                    today = date.today()

                    # daycount日後以前なら continue
                    if (kaisai_date - today).days <= daycount:
                        print("開催日がdaycount日後以前のため飛ばす"+kouenbi_text)
                        continue
                else:
                    print("日付が抽出できません:", kouenbi_text)
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


                    text=eventName_txt+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl+"///"+eventName

                    if "○" in iconStr and "×" not in iconStr:
                        print(text)
                        data=data+text+"\n"
                    
        else:
            eventName_detail=eventsoup.find('p', attrs={ 'class': ['eventName'] } ).text

        


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
            kouenbi_text = kouenbi_text.replace(" ", "")
            kouenbi_text = re.sub(r"\s+", "", kouenbi_text)      
            kouenbi_text = unicodedata.normalize("NFKC", kouenbi_text)

            # 空白（半角・全角・不可視）を削除
            kouenbi_text = re.sub(r"[\s\u200b\u00a0]", "", kouenbi_text)

            # 日本語の曜日を削除（（日）（月）など）
            kouenbi_text = re.sub(r"[（(][日月火水木金土][）)]", "", kouenbi_text)


            # ① 日付部分だけ抽出（例: 2026/01/18）
            print("check:"+repr(kouenbi_text))
            m = re.search(r"(\d{4})\D+(\d{1,2})\D+(\d{1,2})", kouenbi_text)
            if m:
                date_str = m.group()
                kaisai_date = datetime.strptime(date_str, "%Y/%m/%d").date()
                today = date.today()

                # 2日後以前なら continue
                if (kaisai_date - today).days <= 3:
                    print("開催日が3日後以前のため飛ばす"+kouenbi_text)
                    continue
            else:
                print("日付が抽出できません:", kouenbi_text)
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


                text=eventName_txt+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl+"///"+eventName

                if "○" in iconStr and "×" not in iconStr:
                    print(text)
                    data=data+text+"\n"
                



# ディレクトリとファイル名を分離
directory, filename = os.path.split(filepath)

add_filename = f"追加_{filename}"
add_filepath = os.path.join(directory, add_filename)

delete_filename = f"削除_{filename}"
delete_filepath = os.path.join(directory, delete_filename)



# ファイルが存在しているかチェック
if os.path.exists(filepath):
  


    # 新しいファイル名を作成
    before_filename = f"{now_str}_{filename}"
    before_filepath = os.path.join(directory, before_filename)




    # リネーム
    os.rename(filepath, before_filepath)
    print(f"既存ファイルをリネームしました → {before_filepath}")


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

else:
    print("既存ファイルはありません。")

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
