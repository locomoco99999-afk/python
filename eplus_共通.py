import traceback
from selenium import webdriver
from datetime import datetime, date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import unicodedata
import re
from datetime import datetime
import time

import sys
import os
import json
import pickle


from selenium.common.exceptions import NoSuchElementException  # ← これを追加！


from bs4 import BeautifulSoup

import tkinter as tk
import time
import subprocess

import re
import requests
import os
from datetime import datetime, date
from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
driver_path = 'C:/python/chrome/chromedriver.exe'  # パスを書き換えて下さい



SERVICE_KEY =""


service = fs.Service(executable_path=driver_path)

browser = webdriver.Chrome(options=option, service=service)



headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Mobile/15E148 Safari/604.1"
    )
}

BASE_URL = "https://eplus.jp/"

#eventKbn = input("eplus共通 処理を選択してください:1=プロレス ")
eventKbn="1"
if eventKbn=="1" :
    janru=""
    eventNameTittle="プロレス"
    baseFolder="eplus"
else :
    print("その他の入力、終了します。")
    quit()

folder_path_moto= "C:/python/eplus/"+eventNameTittle
filepath='C:/python/eplus/'+eventNameTittle+'/'+eventNameTittle+'.txt'
folder_path = "C:/python/eplus/"+eventNameTittle+"/endcnt"
configfile=folder_path_moto+"/設定/設定ファイル.txt"
configfile_team=folder_path_moto+"/設定/設定_チームリスト.txt"
configfile_team_eigo=folder_path_moto+"/設定/設定_チーム英語リスト.txt"
configfile_ng=folder_path_moto+"/設定/設定_NG席リスト.txt"
configfile_seat=folder_path_moto+"/設定/設定_座席リスト.txt"

os.makedirs(folder_path, exist_ok=True)
filepath_cnt = f"{folder_path}/endcnt_"+eventNameTittle+".txt"

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
        detaildata=""
        try:
            teamName=teams[0]
            team_url=teams[1]


            TARGET_URL = BASE_URL + team_url
            print(TARGET_URL)
            browser.get(TARGET_URL)
            print(eventName)


            #session = requests.Session()
            #session.headers.update(headers)

            #response = session.get(TARGET_URL, timeout=10)


            #タグを整形
            #soup = BeautifulSoup(response.content, "html.parser")


            #aタグ取得
            #aTags = soup.find_all('a', attrs={ 'class': ['ticket-item ticket-item--kouen'] } )
            aTags = browser.find_elements(By.CSS_SELECTOR, "a.ticket-item.ticket-item--kouen")

            linkList=[]
            #リンクを繰り返し
            for atag in aTags:
                linkList.append(atag.get_attribute("href"))
                
            count=0
            for count in range(len(linkList)):
                targetUrl=linkList[count]
                browser.get(targetUrl)
                print(targetUrl)
            #session = requests.Session()
            #session.headers.update(headers)

            #atagresponse = session.get(targetUrl, timeout=10)
            #ページ取得

            
            #タグを整形
            #atagsoup = BeautifulSoup(atagresponse.content, "html.parser")

        

            #sectionList = atagsoup.find_all("section", class_="block-ticket")
            sectionList =  browser.find_elements(By.CSS_SELECTOR, ".block-ticket")


            for list in sectionList:
       
                    title_tag = list.find_element(By.CSS_SELECTOR, "h4.block-ticket__title")
                    if title_tag and "一般発売" in title_tag.text:

                        # 受付中か確認
                        status_div = list.find_element(By.CSS_SELECTOR, "div.block-ticket__status")   
                        if status_div:
                            status_text = status_div.text

                            # どれか1つでも受付中があればOK
                            if  "受付中" in status_text:

                                print("一般発売 & 受付中 → OK")

                                # 次へボタンからURL取得
                                button = list.find_element(By.CSS_SELECTOR, "button.button--primary")     
                                if button and button.get_attribute("onclick"):
                                    button.click()

                                    #詳細画面へ遷移しました

                                        #detailUrlResponse = session.get(detailUrl, timeout=10)
                            
                                        #タグを整形
                                        #detailSoup = BeautifulSoup(detailUrlResponse.content, "html.parser")

                            
                                        #seatCharge=detailSoup.find("div", class_="seat-charge")

                                                    # table 要素取得
                        
                                    kaijo = browser.find_element(By.CSS_SELECTOR, 'span[data-wovn-ignore="true"]').text
                                    kouenbi_jikan=target_td = browser.find_element(By.XPATH,'//div[@class="event-info"]//tr[th[text()="受付開始日時"]]/td').text
                                    kouenbi, kaien_jikan = kouenbi_jikan.split() 
                                    seatcharge=browser.find_element(By.CSS_SELECTOR, "div.seat-charge").text
                                    eventName=elem = browser.find_element(By.CSS_SELECTOR,'span[data-wovn-ignore="true"]').text


                                        # table を取得
                                    table = browser.find_element(By.CSS_SELECTOR, "div.seat-info table")

                                    rows = table.find_elements(By.CSS_SELECTOR, "tr")

                                    seat_status_list = []

                                    # 1. ヘッダー取得
                                    header_ths = rows[0].find_elements(By.CSS_SELECTOR, "th")
                                    seat_names = [th.text.strip() for th in header_ths]

                                    print("列名:", seat_names)

                                     # 空席の td （×, △, △, ○）
                                    header_tds = rows[1].find_elements(By.CSS_SELECTOR, "td")
                                    kuusekis = [td.text.strip() for td in header_tds]

                                    print("空席:", kuusekis)


                                    columnscount=0
                                    for columnscount in range(len(seat_names)):
                                        seat=seat_names[columnscount]
                                        if seat=='公演日時' or seat=='備考':
                                            continue
                                        kuuseki=kuusekis[columnscount-1]

                                        pattern = rf"^{seat}：¥[\d,]+"
                                        match = re.search(pattern, seatcharge, re.MULTILINE)


                                        price=seatcharge
                                        if match:
                                            price = match.group()
                                            print(price)  # → 'Ａシート：¥12,000'


                                        if kuuseki=='○':
                                            print("せきあり")
                                            text=teamName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+kuuseki+"///"+seat+"///"+price+"///"+browser.current_url+"///"+eventName
                                            print(text)
                                            data=data+text+"\n"
                                        columnscount=columnscount+1
            count=count+1  
        except Exception as e:
            print("エラー発生:", e)
            traceback.print_exc() 
            continue

          

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
