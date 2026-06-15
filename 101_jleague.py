import subprocess
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
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


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
import re
import requests
import os
from datetime import datetime, date
from bs4 import BeautifulSoup
import json

#cookies_file = 'C:/python/brave/morokoshi.pkl'
cookies_file = 'C:/python/chrome/morokoshi.pkl'

folder_path_moto= "C:/python/jleague/"
filepath = "C:/python/jleague/jleague.txt"




# Brave本体が、保存されているパスを入力
#option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'  # Windowsの場合
#option.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  # Windowsの場合



# WebDriverを保存したファイルパスを入力
#driver_path = 'C:/python/brave/chromedriver.exe'  # パスを書き換えて下さい
#driver_path = 'C:/python/chrome/chromedriver.exe'  # パスを書き換えて下さい

#api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')


SERVICE_KEY =""
#SITEKEY='6LcnF3snAAAAAC0UQfNtqE2lUKxcPrNgPBzvPT7q'

#chrome://version

#service = fs.Service(executable_path=driver_path)

#browser = webdriver.Chrome(options=option, service=service)

folder_path = "C:/python/jleague/endcnt"
os.makedirs(folder_path, exist_ok=True)
#today = datetime.now().strftime("%Y%m%d")
filepath_cnt = f"{folder_path}/endcnt_jleague.txt"

# ディレクトリとファイル名を分離
directory, filename = os.path.split(filepath)



# 現在時刻を YYYYMMDD_HHMMSS の形式で取得
now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
sabun_txt='C:/python/jleague/差分_'+now_str+'_jleague.txt'



before_filename=""
before_filepath=""


add_filename=""
add_filepath=""
delete_filename=""
delete_filepath=""




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


service = fs.Service(executable_path=driver_path)

browser = webdriver.Chrome(options=option, service=service)


BASE_URL = "https://www.jleague-ticket.jp/"

data=""

configfile=folder_path_moto+"/設定/設定ファイル.txt"
configfile_team=folder_path_moto+"/設定/設定_チームリスト.txt"
configfile_team_eigo=folder_path_moto+"/設定/設定_チーム英語リスト.txt"
configfile_ng=folder_path_moto+"/設定/設定_NG席リスト.txt"
configfile_seat=folder_path_moto+"/設定/設定_座席リスト.txt"
with open(configfile_team, "r", encoding="utf-8-sig") as f:
    config_team = json.load(f)
team_lists = config_team["team_lists"]

    

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
    eventName=teams[0]
    team_url=teams[1]




    TARGET_URL = BASE_URL + team_url+"/"
    print(TARGET_URL)

    print(eventName)
    #ページ取得


    #seleniumはやめた
    #browser.get(TARGET_URL)
    #response = browser.page_source
    browser.get(TARGET_URL)
#    response = requests.get(TARGET_URL)


    #タグを整形
    #soup = BeautifulSoup(response.content, "html.parser")

    li_tags = []

    game_list = browser.find_element(By.CSS_SELECTOR, "div.game-list")
    game_li=game_list.find_elements(By.CSS_SELECTOR, "li")
    game_count=len(game_li)

    if game_count==0:
        continue

    for li_idx in range(game_count):  
        browser.get(TARGET_URL)
        game_list = browser.find_element(By.CSS_SELECTOR, "div.game-list")
        game_li=game_list.find_elements(By.CSS_SELECTOR, "li")
        get_li = game_li[li_idx]


        place_divs = get_li.find_elements(By.CSS_SELECTOR, "div.vs-box")
        if not place_divs:
            continue

        place_div = place_divs[0]

        place_text = place_div.text.strip()
        if "box" in place_text:
            continue
        if "駐車券" in place_text:
            continue

        status_div = get_li.find_element(By.CLASS_NAME, "comp-status")

    
        if status_div:
            status_text = status_div.text.strip()

            if status_text == "空席あり":

                # チケット購入の <span> を取得
                span =  get_li.find_element(By.CLASS_NAME, "ticket-status")
                
                if span and span.get_attribute("href") is not None:
                    link = span.get_attribute("href")
         
                    kobetu_url=BASE_URL+link
                    kobetu_url = (BASE_URL + link).replace("//", "/")
                    print(kobetu_url)
                    browser.get(kobetu_url)
                    
#                    soup2 = BeautifulSoup(response2.content, "html.parser")

                    kaijo_span = browser.find_element(
                        By.CSS_SELECTOR,
                        "div.game-info-stat-place span:first-child"
                    )

                    kaijo = kaijo_span.text.strip()
                    print(kaijo)

                    #公演日
                    # div.game-info
                    hiduke_div = browser.find_element(By.CSS_SELECTOR, "div.game-info")

                    # span.day
                    days = hiduke_div.find_elements(By.CSS_SELECTOR, "span.day")
                    kouenbi = days[0].text.strip() if days else None

                    # span.time
                    times = hiduke_div.find_elements(By.CSS_SELECTOR, "span.time")
                    kaien_jikan = times[0].text.strip() if times else None

                    # 日付変換
                    if kouenbi:
                        kaisai_date = datetime.strptime(kouenbi, "%Y/%m/%d").date()
                    else:
                        kaisai_date = None

                    today = date.today()


                    # div.seat-select-list の中の dl を取得
                    seat_list_divs = browser.find_elements(By.CSS_SELECTOR, "div.seat-select-list")

                    seat_count = len(seat_list_divs)

                    for seatidx in range(seat_count):
                        ##再取得
                        seat_list_divs = browser.find_elements(By.CSS_SELECTOR, "div.seat-select-list")
                        seat_div=seat_list_divs[seatidx]
                        dls = seat_div.find_elements(By.TAG_NAME, "dl")

                        dl_count = len(dls)
                        for dlidx in range(dl_count):

                            ##再取得
                            #seat_list_divs = browser.find_elements(By.CSS_SELECTOR, "div.seat-select-list")
                            #seat_div=seat_list_divs[seatidx]
                            #dls = seat_div.find_elements(By.TAG_NAME, "dl")
                            #dd=dls[dlidx].find_element(By.TAG_NAME, "dd")
                            
                            # 空席ステータス（画像があるか）
                            dl=dls[dlidx]

                            if not dl.find_elements(By.CSS_SELECTOR, "div.seat-select-list-img"):
                                continue

                            # 席種名ブロック
                            name_divs = dl.find_elements(By.CSS_SELECTOR, "div.seat-select-list-txt")
                            if not name_divs:
                                continue
                            seat_name_div = name_divs[0]

                            # h4（席種名）
                            h4s = seat_name_div.find_elements(By.TAG_NAME, "h4")
                            if not h4s:
                                continue
                            seat_name = h4s[0].text.strip()





                            # リセール除外
                            if "リセール" in seat_name:
                                continue

                            # dd（チケット詳細）
                            dd = dl.find_element(By.TAG_NAME, "dd")
                    
                            # li（券種行）
                            seat_status_rows = dl.find_elements(By.TAG_NAME, "li")


                            satus_count = len(seat_status_rows)
                            for stsidx in range(satus_count):

                                #seat_list_divs = browser.find_elements(By.CSS_SELECTOR, "div.seat-select-list")
                                #seat_div=seat_list_divs[seatidx]

                                #dls = seat_div.find_elements(By.TAG_NAME, "dl")
                                #dl=dls[dlidx]
                                #dd=dls[dlidx].find_element(By.TAG_NAME, "dd")
                                #seat_status_rows = dl.find_elements(By.TAG_NAME, "li")


                                # 空席ステータス（画像があるか）
                                row=seat_status_rows[stsidx]
                               
    

                                few_imgs = row.find_elements(
                                    By.CSS_SELECTOR,
                                    'img[src*="ico_few"]'
                                )

                                if few_imgs:
                                    continue
                                        
                                # 満席（bg-no）スキップ
                                if row.find_elements(
                                    By.CSS_SELECTOR,
                                    'img[src*="ico_no"]'
                                ):
                                    continue
               
                                a_tag = row.find_element(By.TAG_NAME, "a")
                                browser.execute_script("arguments[0].scrollIntoView({block:'center'});", a_tag)
                                time.sleep(0.5)

                                browser.execute_script("arguments[0].click();", a_tag)
                                
                                
                                
                                try:
                                    qr_button = WebDriverWait(browser, 5).until(
                                        EC.presence_of_element_located((By.ID, "delivery_type_qr"))
                                    )
                                    qr_button.click()
                                
                                except Exception:
                                    # QRボタンが無い → 次へ
                                    btn = browser.find_element(By.CSS_SELECTOR, ".js-modalClose")
                                    browser.execute_script("arguments[0].click();", btn)
                                    continue
                            
                                print("QRボタンクリック")              
                                time.sleep(0.5)   
                                def get_span_when_has_text(driver):
                                    try:
                                        el = driver.find_element(
                                            By.CSS_SELECTOR,
                                            "li.modal-cts-slider-item.active div.assign h4 span"
                                        )
                                        if el.is_displayed() and el.text.strip():
                                            return el
                                        return False
                                    except (StaleElementReferenceException, NoSuchElementException):
                                        return False
                            
                                try:
                                    span = WebDriverWait(browser, 10).until(get_span_when_has_text)
                                    print(span.text)
                                except TimeoutException:
                                    continue
                            
                                zone = span.text
                                print(zone)
                        

                                seat_lists = browser.find_elements(By.CSS_SELECTOR, "div.release-item")

                                for seat_list in seat_lists:

                                    releas_div= seat_list.find_element(By.CSS_SELECTOR, "div.release-desc")

                                    seat_tittle=releas_div.find_element(By.CSS_SELECTOR, "h5.release-title").text

                                    if "ＱＲ" not in seat_tittle:
                                        continue
                                    
                                    if "一般" not in seat_tittle:
                                        continue

                                    price=releas_div.find_element(By.CSS_SELECTOR, "p.release-price").text
                                                                        
                                    img = seat_list.find_element(By.CSS_SELECTOR, "img.release-icon")
                                    src = img.get_attribute("src")


                                    if not src.endswith("/img/ico_vacant.svg"):
                                        continue

                                    kuuseki="〇"

                                    text=eventName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+kuuseki+"///"+zone+"///"+price+"///"+browser.current_url+"///"+eventName
                                    print(text)
                                    data=data+text+"\n"
                                btn = browser.find_element(By.CSS_SELECTOR, ".js-btn-slide")
                                browser.execute_script("arguments[0].click();", btn)
                                btn = browser.find_element(By.CSS_SELECTOR, ".js-modalClose")
                                browser.execute_script("arguments[0].click();", btn)
      
                                    
                                
                                
                                



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

    with open(add_filepath, "w", encoding="utf-8") as f:
        f.write("")

    with open(delete_filepath, "w", encoding="utf-8") as f:
        f.write(data)


