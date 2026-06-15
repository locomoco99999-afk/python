import traceback
import re
import requests
import os
from datetime import datetime, date
from bs4 import BeautifulSoup
janru="s/113193/d"
BASE_URL = "https://7ticket.jp/"




#出力データ
data=""


TARGET_URL = BASE_URL + janru
    
print(TARGET_URL)
eventName="木下大サーカス"
print(eventName)

#ページ取得
response = requests.get(TARGET_URL)


#タグを整形
soup = BeautifulSoup(response.content, "html.parser")

#aタグ取得
links = soup.find_all("a")

#リスト
eventList = []


filepath='C:/python/7ticket/7ticket_circusIwata.txt'
folder_path = "C:/python/7ticket/endcnt"
os.makedirs(folder_path, exist_ok=True)
#today = datetime.now().strftime("%Y%m%d")
filepath_cnt = f"{folder_path}/endcnt_7ticket_circusIwata.txt"




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


                text="木下大サーカス"+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl+"///"+eventName

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


            text="木下大サーカス"+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr[1:]+"///"+priceStr+"///"+eventUrl+"///"+eventName

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
