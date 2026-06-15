import requests


from bs4 import BeautifulSoup

janru="stage"
TARGET_URL = "https://t.pia.jp/"+janru




#出力データ
data=""




#ページ取得
response = requests.get(TARGET_URL)


janru=janru.replace('/', '-')
filepath='C:/python/piaweb/' + janru + '.txt'

#タグを整形
soup = BeautifulSoup(response.content, "html.parser")

#aタグ取得
links = soup.find_all("a")

#リスト
eventList = []




#リンクを繰り返し
for link in links:

    #eventBundleCdを指定
    if 'eventBundleCd' in link.attrs['href']:
        
        #リンクを出力
      # print(link.attrs['href'])

       #リストに追加
       eventList.append(link.attrs['href'])
    

#イベント件数取得
eventKensu=len(eventList)
print(eventKensu)


#件数分繰り返し
for i in range(eventKensu):
#   print(eventList[i])

    #1つずつイベント指定
    eventUrl=eventList[i]
    # print(eventUrl)

    #ページ取得
    eventResp = requests.get(eventUrl, timeout=(3.0, 7.5))
    #print(eventResp )

    #タグを整形
    eventSoup = BeautifulSoup(eventResp.content, "html.parser",from_encoding='utf-8')
    #eventSoup = BeautifulSoup(eventResp.content,'lxml')

    #sales=eventSoup.find('div', id="sales_content")
    sales=eventSoup.find_all('li', attrs={ 'class': ['ticketSalesList-2024__item vevent','vevent'] } )
    #文字連結
    #data=data+sales.get_text() 





    #1チケットずつ処理したいので行単位で取得する
    #data=data+eventUrl+"\n"
    for row in sales:

        #抽選と紙は除く
        if "終了" not in row.text and "紙" not in row.text and "抽選" not in row.text and "車いす" not in row.text:

            print( row.text)

            tittles=row.select('.ticketSalesCard-2024__title')
            tittle_=""
            for tittle in tittles:
                tittle_=tittle_+tittle.getText().replace(' ', '').replace('\n', '')
                #if eventUrl in "http:t.pia.jp/pia/event/event.do?eventBundleCd=b2344517":
                #    print(eventUrl)
                #    print(tittle.contents)



            date=row.find(True, attrs={ 'class': ['ticketSalesCard-2024__date'] } ).getText().replace(' ', '').replace('\n', '')
          
           # dtend=row.find(True, attrs={ 'class': ['dtend'] } ).getText().replace(' ', '').replace('\n', '')
            places=row.select('.ticketSalesCard-2024_place')
            place_=""
            for place in places:
                place_=place_+place.getText().replace(' ', '').replace('\n', '')
           
        
            states=row.select('.Y15-is-state')

            status=""
            for state in states:
                status=status+state.getText().replace(' ', '').replace('\n', '')

        
            #ブランク削除し、区切りを入れる
            #data=data+eventUrl+"\n"
            text=tittle_+"///"+date+"///"+place_+"///"+status
            #data=data+text+"\n"

            

            details = row.find_all("a", limit=1)
            
            ##data=data+"row"+row.text

            detailUrl=""
            for detail in details:
       
       
                #詳細画面
                if 'lotRlsCd' in detail.attrs['href'] or 'rlsCd' in detail.attrs['href']:
                    detailUrl=detail.attrs['href']

                    #data=data+detailUrl+"\n"

                     #ページ取得
                    detailPage = requests.get(detailUrl, timeout=(3.0, 7.5))
            

                    #タグを整形
                    detailSoup = BeautifulSoup(detailPage.content, "html.parser",from_encoding='utf-8')
                    #detailSoup = BeautifulSoup(detailPage.content,'lxml')

                    ##data=data+"detailSoup"+detailSoup.text


                    #print(detailUrl)
                    #print(detailSoup.contents)
                    datetime_sections=detailSoup.select('.Y15-regular-section')

                  

  

                    for datetime_section in datetime_sections:
                  
                        #print("datetime_sectionきた")
                        
                        #data=data+"datetime_section"+"\n"
                        #data=data+datetime_section.text.replace('  ', ' ').replace('\n', '')

    



                        datetime_headers=datetime_section.select('.Y15-event-datetime-header')
                        datetime_header_=""
                        for datetime_header in datetime_headers:
                            datetime_header_=datetime_header_+datetime_header.getText().replace(' ', '').replace('\n', '')
               
                        #data=data+"日付:"+datetime_header_+"\n"
                        #print("日付:"+datetime_header_)
                        sheats=datetime_section.select('.ticketSelect__text')
                        sheat_=""
                        for sheat in sheats:
                            sheat_=sheat_+sheat.getText().replace('  ', ' ').replace('\n', '')
                            data=data+"★"+text+"日付+座席:"+datetime_header_+"///"+sheat_+"/"+detailUrl+"\n"


                        #if detailUrl in "https://t.pia.jp/pia/ticketInformation.do?lotRlsCd=52702":
                        #    print(detailUrl)
                        #    print("★日付+座席:"+datetime_header_+"/"+sheat_+"\n")




#出力
#print(data)






# ファイルを開く
with open(filepath, 'w+',encoding='UTF-8') as file:

    # 文字列をファイルに書き込む
    file.write(data)
    file.close
        

    




 

