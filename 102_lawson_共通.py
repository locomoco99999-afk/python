from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from selenium import webdriver
from datetime import datetime, date,timedelta
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
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "ja-JP,ja;q=0.9",
    "Connection": "keep-alive",
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
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'  # Windowsの場合
option.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  # Windowsの場合



# WebDriverを保存したファイルパスを入力
driver_path = 'C:/python/chrome/chromedriver.exe'  # パスを書き換えて下さい



SERVICE_KEY =""


service = fs.Service(executable_path=driver_path)

browser = webdriver.Chrome(options=option, service=service)




BASE_URL = "https://l-tike.com/"

eventKbn = input("ローソン 処理を選択してください:1=プロレス,2=卓球 ,3=相撲,4=アイススケート,5=野球,6=六大学野球2026 ")

if eventKbn=="1" :
    janru=""
    eventNameTittle="プロレス"
    baseFolder="lawson"

elif eventKbn=="2" :
    janru=""
    eventNameTittle="卓球"
    baseFolder="lawson"
elif eventKbn=="3" :
    janru=""
    eventNameTittle="相撲"
    baseFolder="lawson"
elif eventKbn=="4" :
    janru=""
    eventNameTittle="アイススケート"
    baseFolder="lawson"
elif eventKbn=="5" :
    janru=""
    eventNameTittle="野球"
    baseFolder="lawson"
elif eventKbn=="6" :
    janru=""
    eventNameTittle="ローソン大学野球2026"
    baseFolder="lawson"
else :
    print("その他の入力、とりあえず野球にします。")
    janru=""
    eventNameTittle="野球"
    baseFolder="lawson"


folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
filepath='C:/python/'+baseFolder+'/'+eventNameTittle+'/'+eventNameTittle+'.txt'
folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
configfile=folder_path_moto+"/設定/設定ファイル.txt"
configfile_team=folder_path_moto+"/設定/設定_チームリスト.txt"
configfile_team_eigo=folder_path_moto+"/設定/設定_チーム英語リスト.txt"
configfile_ng=folder_path_moto+"/設定/設定_NG席リスト.txt"
configfile_seat=folder_path_moto+"/設定/設定_座席リスト.txt"

os.makedirs(folder_path, exist_ok=True)
filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"

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
        teamName=teams[0]
        team_url=teams[1]


        TARGET_URL = BASE_URL + team_url
        print(TARGET_URL)
    
        browser.get(TARGET_URL)
        tagList=[]


        try:


            ticket_kochira = browser.find_element(By.CSS_SELECTOR, "a.cv-link")

            print("チケットはこちらをクリック")
            #ticket_kochira.click()
            # href を取得
            ticket_url = ticket_kochira.get_attribute("href")

            if "l-tike.com/order/" not in ticket_url:
                print(ticket_url+"は違うサイトだからとばす　Xのリンクとか")
                #エラーを発火
                raise ValueError(ticket_url+"は違うサイトだからとばす　Xのリンクとか")
           
            else:


                # href に直接遷移
                browser.get(ticket_url)
                
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )           
                wait = WebDriverWait(browser, 30)
                divslist = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.ResultBox__table")))
                

                i = -1
                while i < len(divslist) - 1:
                    i += 1
                    div = divslist[i]
                    salesName=div.find_element(By.ID, "sale_name")
                    if "一般発売" in salesName.text:

                        try:
                            wait = WebDriverWait(div, 45)
                            a_tag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.entryBtn")))

                            tempUrl=browser.current_url
                            print("申し込みはこちらをクリック")

                            a_tag.click()
                            tagList.append(browser.current_url)
                            browser.get(tempUrl)
        
                            divslist = browser.find_elements(By.CSS_SELECTOR, "div.ResultBox__table")
                        except Exception as e:
                            traceback.print_exc() 

                            print("申し込みはこちらはなし2")
            
        except Exception as e:
            traceback.print_exc() 

            print("チケットはこちらはなし")

            
            
    
    
            try:
                browser.switch_to.default_content()
    

                a_tags = browser.find_elements(By.CSS_SELECTOR, "a.lt-ticket-list-link")


                for a in a_tags:
                                    
                    hanabiKbn = a.find_element(
                        By.CSS_SELECTOR,
                        "span.lt-ticket-list-item__options-basic"
                    )   
                    if "一般発売" not in hanabiKbn.text:
                        print("一般発売でない"+hanabiKbn.text)
                    else:
                        astatus = a.find_element(
                            By.CSS_SELECTOR,
                            "span.lt-ticket-list-item__status"
                        ).text

                        print(astatus)
                        if "発売中" in astatus :
                            tagList.append(a.get_attribute("href"))
            except Exception as e:
                traceback.print_exc() 
                print("販売リンクが１つもない")
                continue



        print(len(tagList))

        for href in tagList:
            print(href)
            browser.get(href)
           
            try:
                wait = WebDriverWait(browser, 30)
                divss = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.AccordionBox__inner")))
                     
            except Exception as e:
                print("取得できないので次へ")
                continue


            for div in divss:
                wait = WebDriverWait(browser, 10)


                toggle_btn=div.find_element(By.CSS_SELECTOR, 'button.AccordionToggleButton')
       
                aria_expanded = div.get_attribute("aria-expanded")

                if aria_expanded == "true":
                    browser.execute_script("arguments[0].click();", toggle_btn)
            
                lis = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.AccordionBox__item")))
                for li in lis:
                    kouenbi=browser.find_element(By.CSS_SELECTOR, 'p.AccordionBox__date').text

                    kaisaibi=kouenbi
                    kaisaibi = re.sub(r'\(.+?\)', '', kaisaibi)
                    m = re.search(r"(\d{4})/(\d{1,2})/(\d{1,2})", kaisaibi)


                    kaisaidatesplit=kaisaibi.split("/")
                    kaisaidate = datetime(
                        int(kaisaidatesplit[0]), 
                        int(kaisaidatesplit[1]), 
                        int(kaisaidatesplit[2])
                    )

                    limit_date = datetime.today() + timedelta(days=daycount)

                    # もし開催日が今日+daycount 以前ならスキップ
                    if kaisaidate <= limit_date:
                        print("今日+daycount 以前ならスキップ")
                        continue



                    kaien_jikan=div.find_element(By.CSS_SELECTOR, 'ul.AccordionBox__time').text
                    kaien_jikan=kaien_jikan.replace("\n", "-")
                    
                    eventName=browser.find_element(By.CSS_SELECTOR, 'h3.AccordionBox__title').text
                    kaijo=browser.find_element(By.CSS_SELECTOR, 'p.AccordionBox__place').text
                    seat_name = li.get_attribute('data-name')
                    price = li.find_element(By.CSS_SELECTOR,'p.AccordionBox__itemPrice').text
                    kuuseki = li.find_element(By.CSS_SELECTOR,'p.AccordionBox__itemStatus').text

                    if any(ng in seat_name for ng in ngwords):
                        print("NG席なので飛ばします"+seat_name)
                        continue

                    # チケット判定
                    if kuuseki == "発売中":

                        
                        
   
                        event_comment = wait.until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, "section.eventComment")
                            )
                        )

                        event_comment_text = event_comment.text
                        print(event_comment_text)

                        if "電子チケット" in event_comment_text and  "電子チケットの分配が可能" not in event_comment_text :
                            continue

                        if  "身分証明書" in event_comment_text and event_comment_text not in "身分証明書のご提示をお願いする場合がございます。":
                            continue



                        print("せきあり")
                        print(seat_name)
                        text=teamName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+kuuseki+"///"+seat_name+"///"+price+"///"+browser.current_url+"///"+eventName
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

print("終了しました")

#プログラムが終了すると勝手に閉じてしまう
#time.sleep(1000000)

browser.quit()



