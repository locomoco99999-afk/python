from selenium import webdriver
from datetime import datetime, date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select
import unicodedata
import re
from datetime import datetime
import time

import sys
import os

import pickle


from selenium.common.exceptions import NoSuchElementException  # ← これを追加！


from bs4 import BeautifulSoup

import tkinter as tk


#cookies_file = 'C:/python/brave/morokoshi.pkl'
cookies_file = 'C:/python/chrome/morokoshi.pkl'


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



browser.get(SITEURL+KEISAIURL)
time.sleep(1)   

filepath='C:/python/7ticket/delete_7ticket_circusTachikawa.txt'



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

event="木下大サーカス"

#座席の紐づけマップ
seat_map = {
    "リングサイドA": ["リングサイドA","ring sideA","Ringside A + Admission ticket"],
    "リングサイドB": ["リングサイドA","ring sideB","Ringside B + Admission ticket"],
    "リングサイドC": ["リングサイドA","ring sideC","Ringside C + Admission ticket"],
 
   "ロイヤルブルー": ["ロイヤルブルー","Royal Blue","Royal Blue + Admission ticket"],
   "ロイヤルイエロー": ["ロイヤルイエロー","Royal Yellow","Royal Yellow + Admission ticket"],
   "ロイヤルグリーン": ["ロイヤルグリーン","Royal Green","Royal Green + Admission ticket"],


 
 }


service = fs.Service(executable_path=driver_path)

browser = webdriver.Chrome(options=option, service=service)



browser.get(SITEURL+KEISAIURL)
time.sleep(1)   

print("mainGrid =", len(browser.find_elements(By.ID, "mainGrid")))
print("rows =", len(browser.find_elements(By.CSS_SELECTOR, "tr.group.eventRow")))

iframes = browser.find_elements(By.TAG_NAME, "iframe")
print("iframe count =", len(iframes))


html = browser.find_element(By.CSS_SELECTOR, "#mainGrid tbody").get_attribute("innerHTML")
print(html)

time.sleep(2)  



txtSearch = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID,"search"))
)

txtSearch.send_keys(event)
time.sleep(2)


txtSearch.send_keys(Keys.ENTER)
time.sleep(3)





count=0
rows = WebDriverWait(browser, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.group.eventRow"))
)

print("row count =", len(rows))

  
time.sleep(1)




print("行数:", len(rows))


print(filepath)
lines = []
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

count=0
while count<len(lines):

    s_line = lines[count].strip()
    data=s_line

    array = data.split("///")

    eventName=array[0]
    kaijo=array[1]
    kaisaibi=array[2]
    jikan=array[3]
    jyokyo=array[4]
    sheet=array[5]

    if "リングサイド" in sheet:        
        print("リングサイドはいったんスルー")
        count=count+1
        continue
    else :
        print(sheet)


      #  targetSheet=seat
    for row in rows:
        try:

            print(row.text)


                #削除済みのものだけ
            # sold = 0 の時だけ check ボタン取得

         

            # 曜日の（〜）を削除
            clean = kaisaibi.split("（")[0]

            # 日付部分を分割
            y, m, d = clean.split("/")

            # 整形
            kaisaibi_text = f"{y}年 {int(m)}月 {int(d)}日"

            print(kaisaibi_text)

       
          
            if kaisaibi_text in row.text and jikan in row.text and eventName in row.text:
                
    

                event_id = row.get_attribute("data-eventid")
                multi_selector = f"tr.multi[data-eventlistingslink*='event_id={event_id}']"

                listings =None

                listings = browser.find_elements(By.CSS_SELECTOR, multi_selector)

                if not listings:
                    print("要素が無かった")
                    row.click()
                    listings = WebDriverWait(browser, 1).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, multi_selector))
                    )
                    # 無いときの処理
                else:
                    print("要素があった")
                    # あったときの処理



                for mini in listings:
                    
                   # soldCol を取得 soldoutは除外
                    sold_text = mini.find_element(By.CSS_SELECTOR, "td.soldCol span").text.strip()

                    print("sold =", sold_text)

                    # 0 以外ならスキップ
                    if sold_text != "0":
                        count=count+1
                        continue

                    #シート文字変換パターン
                    values = seat_map[sheet]
                    for seatValue in values:
                        if seatValue in mini.text:

                            class_name = mini.get_attribute("class")

                            # checked が無ければクリックしてチェックを入れる
                            if "checked" not in class_name:


                                btn = mini.find_element(By.CSS_SELECTOR, "td.check.min.pointer.bdrr")

#                                browser.execute_script("arguments[0].scrollIntoView(true);", btn)
                                browser.execute_script("arguments[0].click();", btn)

                                print("clicked")
                      

                    #直接パターン
                    if sheet in mini.text:
                            
                            class_name = mini.get_attribute("class")

                            # checked が無ければクリックしてチェックを入れる
                            if "checked" not in class_name:
                                btn = mini.find_element(By.CSS_SELECTOR, "td.check.min.pointer.bdrr")

                                browser.execute_script("arguments[0].scrollIntoView(true);", btn)
                                browser.execute_script("arguments[0].click();", btn)

                                print("clicked")
                         


        except Exception as e:
            print("error:", e)
    count=count+1

print("終了しました")

#プログラムが終了すると勝手に閉じてしまう
time.sleep(1000000)

browser.quit()