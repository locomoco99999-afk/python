import requests


from bs4 import BeautifulSoup


BASE_URL = "https://7ticket.jp/"




#出力データ
data=""

team_lists = [
    ["読売ジャイアンツ", "g/000156"],
    ["阪神タイガース", "g/000169"],
    ["横浜DeNAベイスターズ", "g/000208"],
    ["広島東洋カープ", "g/000182"],
    ["東京ヤクルトスワローズ", "g/000221"],
    ["中日ドラゴンズ", "g/000195"],
    ["福岡ソフトバンクホークス", "g/000003"],
    ["北海道日本ハムファイターズ", "g/000029"],
    ["千葉ロッテマリーンズ", "g/000043"],
    ["東北楽天ゴールデンイーグルス", "g/000069"],
    ["オリックス・バファローズ", "g/000016"],
    ["埼玉西武ライオンズ", "g/000056"],
]


for teams in team_lists:
    janru=teams[1]
    TARGET_URL = BASE_URL + janru
    teamName=teams[0]
    
    


    #ページ取得
    response = requests.get(TARGET_URL)


    janru=janru.replace('/', '-')
    filepath='C:/python/7ticket/' + janru + '.txt'


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
        eventName=eventsoup.find('p', attrs={ 'class': ['eventName'] } ).text

    
        print(eventName)

        # 1) 全ての dt と dd を順番通りに取得
        items = eventsoup.select("dl.eventInfo dt, dl.eventInfo dd")

        # 2) ペアにして辞書化
        event_info = {}
        for i in range(0, len(items), 2):
            key = items[i].get_text(strip=True)
            value = items[i+1].get_text(strip=True)
            event_info[key] = value

        # 結果
        #kaijo = event_info.get("会場", "")
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


            text=eventName+"///"+teamName+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr+"///"+priceStr

            if "○" in iconStr and "×" not in iconStr:
                print(text)
                data=data+text+"\n"


# ファイルを開く
with open(filepath, 'w+',encoding='UTF-8') as file:

    # 文字列をファイルに書き込む
    file.write(data)
    file.close
    