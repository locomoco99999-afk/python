from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import sys
import os

import pickle


import datetime

from bs4 import BeautifulSoup

import tkinter as tk


#cookies_file = 'C:/python/brave/morokoshi.pkl'
cookies_file = 'C:/python/chrome/morokoshi.pkl'


janru="g-000702.txt"
filepath="C:/python/7ticket/"+janru



#座席の紐づけマップ
seat_map = {
    "○3塁側パフォーマンス": "3rd Base Performance",
   # "○内野自由席":"Infield Unreserved (Upper Deck)",
    "○外野指定席 レフト": "外野指定席 レフト",
    "○外野指定席 ライト": "外野指定席 ライト",
    "○カープパフォーマンスB": "カープパフォーマンスB",
    "○スカイシート 1塁側": "スカイシート 1塁側",
    "○スカイシート 正面1塁寄り": "スカイシート 1塁側",
    "○内野指定席A 1塁側": "内野指定席A 1塁側",
    "○内野指定席A 3塁側": "内野指定席A 3塁側",
    "○ビジターパフォーマンス": "ビジターパフォーマンス"
    
}


team_map = {
    "読売": "ジャイアンツ",
    "阪神": "タイガース",
    "中日": "ドラゴンズ",
    "広島": "カープ",
    "横浜": "ベイスターズ",
    "ヤクルト": "スワローズ"
}

team_map_eigo = {
    "読売":"Giants",
    "阪神":"Tigers",
    "中日":"Dragons",
    "広島":"Carp",
    "横浜":"BayStars",
    "ヤクルト":"Swallows"
}
#listFilepath="C:/python/piaweb/list-sports-baseball-.txt"
##artistListFilepath="C:/python/piaweb/artist_list.txt"

#sheetFilepath="C:\python\piaweb\sheet-sports-baseball-.txt"

option = webdriver.ChromeOptions()
option.debugger_address = "127.0.0.1:9222"
# 既存プロファイルを指定（例：Windowsの場合）
#option.add_argument(r"user-data-dir=C:\Users\locom\AppData\Local\Google\Chrome\User Data")
# 必要ならプロファイル名指定（デフォルトは 'Default'）
#option.add_argument(r"profile-directory=Default")


# Brave本体が、保存されているパスを入力
#option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'  # Windowsの場合
option.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  # Windowsの場合



# WebDriverを保存したファイルパスを入力
#driver_path = 'C:/python/brave/chromedriver.exe'  # パスを書き換えて下さい
driver_path = 'C:/python/chrome/chromedriver.exe'  # パスを書き換えて下さい

#api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')


#SITEURL="https://inv.viagogo.com"
SITEURL="https://inv.viagogo.com/"
KEISAIURL="/Listings"

#ID="fmbt03@yahoo.co.jp"
#PASSWORD="f03"
#ID=""
#PASSWORD=""

SERVICE_KEY =""
#SITEKEY='6LcnF3snAAAAAC0UQfNtqE2lUKxcPrNgPBzvPT7q'

#chrome://version

service = fs.Service(executable_path=driver_path)

browser = webdriver.Chrome(options=option, service=service)



time.sleep(2)

data=""
count=0
##一旦一番最初のデータのみとする
with open(filepath, encoding="utf-8") as f:
    for s_line in f:



        #件数指定
        if count>2:
            break
        
            
        data=s_line


        array = data.split("///")

        eventName=array[0]
        kaijo=array[1]
        kaisaibi=array[2]
        jikan=array[3]
        jyokyo=array[4]
        sheet=array[5]
        targetSheet=seat_map.get(sheet,"")


        price=array[6]
        price = price.strip()
        if any(x in price for x in ["共通", "大人", "一般"]) and all(y not in price for y in ["子供", "駐車場"]):
            print("共通大人一般のみとする。それ以外は一旦スルー:"+price)
            continue


        if targetSheet in "":
            print("シートの登録が無いから次へ:"+targetSheet)
            continue


        browser.get(SITEURL+KEISAIURL)
        time.sleep(4)   

        new_spn_BT=browser.find_element(By.ID,"newListing")
        new_spn_BT.click()
        time.sleep(2)



        parts = eventName.split(" vs ")

        team1 = team_map.get(parts[0],parts[0])   # 広島
        # parts[1]は "巨人 8/26（火）" なので、スペースで分割
        team2_and_date = parts[1].split(" ", 1)
        team2 = team_map.get(team2_and_date[0],team2_and_date[0])  # 巨人 ドラゴンズに変換

        date = team2_and_date[1]  # 8/26（火）

 

      
        browser.execute_script("document.getElementsByClassName('picker__input')[0].removeAttribute('readonly');")
        browser.execute_script("document.getElementsByClassName('picker__input')[1].removeAttribute('readonly');")

        txtSearch=browser.find_element(By.ID,"txtSearch")
        txtSearch.send_keys(team1+" "+team2)


        kaisaidatesplit=kaisaibi.split("/")
        print(kaisaibi)
        print(kaisaidatesplit[0])
   

        #月と日もセット
        kaisaiFrom=kaisaidatesplit[0]+"/"+kaisaidatesplit[1].rjust(2, '0')+"/"+kaisaidatesplit[2][:2]
        kaisaiFrom_2 = (
                        kaisaidatesplit[0] + "年 " +
                        str(int(kaisaidatesplit[1])) + "月 " +
                        str(int(kaisaidatesplit[2][:2])) + "日 "
                        )

        kaisaiFrom_2=kaisaiFrom_2.rstrip()
        print("check:"+kaisaiFrom)
        dateFrom=browser.find_element(By.ID,"dateFrom")
        #dateFrom.__delattr__("readonly")
        dateFrom.click()
        dateFrom.send_keys(kaisaiFrom)

        

        time.sleep(1)

#               
        kaisaiTo=kaisaiFrom
        kaisaiTo_2=kaisaiFrom_2
        print("kaisaibiTo"+kaisaiTo)

        dateTo=browser.find_element(By.ID,"dateTo")
        #dateTo.__delattr__("readonly")
        dateTo.click()
        dateTo.send_keys(kaisaiTo)

        txtSearch.click()
        txtSearch.send_keys(Keys.ENTER)


        #しばらくまつ　早すぎると無理
        time.sleep(5)
        


          ##日程リスト選択
        searchDivElem = browser.find_element(By.ID, "searchGrid")
        trElems = searchDivElem.find_elements(By.CLASS_NAME, "pointer")

        hidukeari=None
        print("kaisaiFrom_2"+kaisaiFrom_2)
        for trElem in trElems:
            print("text"+trElem.text)
            print("kaisaiFrom_2"+kaisaiFrom_2)

            if kaisaiFrom_2  in trElem.text:
                hidukeari=trElem
                print("同じ日付あり")
                
            if kaisaiTo_2  in trElem.text:
                hidukeari=trElem
                print("同じ日付あり")


        #日付が合わない場合
        if hidukeari is None :
             print("同じ日付が見つからなかった")

            #次は英語
             team1 = team_map_eigo.get(parts[0],parts[0])   # 広島
             team2 = team_map_eigo.get(team2_and_date[0],team2_and_date[0])  # 巨人 ドラゴンズに変換
             txtSearch.send_keys(team1+" "+team2)
             txtSearch.click()
             txtSearch.send_keys(Keys.ENTER)



             print("kaisaiFrom_2"+kaisaiFrom_2)
             for trElem in trElems:
                print("text"+trElem.text)
                print("kaisaiFrom_2"+kaisaiFrom_2)

                if kaisaiFrom_2  in trElem.text:
                    hidukeari=trElem
                    print("同じ日付あり")
                
                if kaisaiTo_2  in trElem.text:
                    hidukeari=trElem
                    print("同じ日付あり")


            #日付が合わない場合
             if hidukeari is None :
                  print("同じ日付が見つからなかった")
                  continue                     
             else:
                  hidukeari.click()


        else:
             hidukeari.click()

     




             
  ##ここで待たないとモーダルの内容がとれない
        time.sleep(5)

        content_html=browser.find_element(By.ID, "content")
        print(content_html.text)

        weelem = content_html.find_element(By.CLASS_NAME, "frame")
  

        print(weelem.text)
   
        jsSelects = content_html.find_elements(By.CLASS_NAME, "js-select")

   

        #selecter_item=None
        #for jsSelect in jsSelects:
        #    print("test"+jsSelect.text)

        #    if "紙のチケット"  in jsSelect.text:
        #        selecter_item=jsSelect

              
        #if selecter_item is None :
        #     print("紙のチケットのボタンがない？")
        #     jsSelects[0].click()
        #else:
        #     jsSelect.click()
        browser.find_element(By.CSS_SELECTOR, 'div.tile.press.mbm.js-select[data-type="PaperTicket"]').click()


        time.sleep(4)


        content_html=browser.find_element(By.ID, "content")


        maisuTX = content_html.find_element(By.ID, "Listing_AvailableTickets")
        maisuTX.send_keys("2")

        

        
        
        #非掲載
        toggle_div = content_html.find_element(By.CLASS_NAME, "toggle")
        label_LB = toggle_div.find_element(By.CSS_SELECTOR, 'label[for="IsPublishToViagogo"]')
        label_LB.click()
        #toggle_div=content_html.find_element(By.CLASS_NAME, "toggle")
        
        #label_LB=toggle_div.find_element(By.TAG_NAME,"label")
        #label_LB.click()
        

        ##ここで待たないとモーダルの内容がとれない
        time.sleep(3)


        
        section = content_html.find_element(By.ID, "Listing.Section")
        section.send_keys(targetSheet)

        #section2 = content_html.find_element(By.ID, "Listing_Section")
        #section2.send_keys(targetSheet)



        #uploadCheck=browser.find_element(By.ID, "Listing.PostUploadReservation")
        #Listing_PostUploadReservations=content_html.find_element(By.ID, "Listing_PostUploadReservation")
        #Listing_PostUploadReservations[1].click()


        #checkbox = content_html.find_element(By.ID, "Listing_PostUploadReservation")
        # チェックが入っていない場合のみクリック
        #checkbox.click()

        #browser.find_element(By.CSS_SELECTOR, 'input[name="Listing.PostUploadReservation"][value="True"]').click()


        
        price_int = int(price.replace("共通", "").replace("円", "").replace(",", ""))

        price_int=price_int+2500

        

        priceArea=browser.find_element(By.ID,"Listing_WebsitePrice")
        #dateTo.__delattr__("readonly")
        priceArea.click()
        priceArea.send_keys(price_int)

        priceArea2=browser.find_element(By.ID,"Listing_Proceeds")
        #dateTo.__delattr__("readonly")
        priceArea2.click()
        priceArea2.send_keys(price_int)

        priceArea3=browser.find_element(By.ID,"Listing_FaceValue")
        #dateTo.__delattr__("readonly")
        priceArea3.click()
        priceArea3.send_keys(price_int)


        btnSaveDetails=browser.find_element(By.ID,"btnSaveDetails")
        #dateTo.__delattr__("readonly")
        btnSaveDetails.click()
        btnSaveDetails.send_keys(price_int)


        time.sleep(4)

        btnOk = browser.find_element(By.CSS_SELECTOR, "a.btn.mtxs.js-ok.pri.mbm")
        btnOk.click()

        count=count+1


     #   browser.execute_script("arguments[1].click();", uploadCheck)

#プログラムが終了すると勝手に閉じてしまう
time.sleep(1000000)

browser.quit()