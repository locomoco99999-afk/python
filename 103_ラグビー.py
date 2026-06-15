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


#service = fs.Service(executable_path=driver_path)

#browser = webdriver.Chrome(options=option, service=service)




BASE_URL = "https://ticketrugby.jp/"


eventKbn="1"
if eventKbn=="1" :
    janru=""
    eventNameTittle="ラグビー"
    baseFolder="ラグビー"




folder_path_moto= "C:/python/"+baseFolder
filepath='C:/python/'+baseFolder+'/'+eventNameTittle+'.txt'
folder_path = "C:/python/"+baseFolder+"/endcnt"
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
#リスト




TARGET_URL = BASE_URL + "ticket_schedule.html"
print(TARGET_URL)


eventList=[]


#ページ取得
response = requests.get(TARGET_URL)


#タグを整形
soup = BeautifulSoup(response.content, "html.parser")
#aタグ取得
links = soup.find_all('a')

for a in links:
    if a.text.strip() == "発売中":
        href = a.get('href')
        if href:
            print(href)
            eventList.append(href)


eventKensu=len(eventList)

#1チームずつ開催日分まとめて　座席一覧繰り返し
for i in range(eventKensu):
#   print(eventList[i])

    #1つずつイベント指定
    eventUrl=eventList[i]
    # print(eventUrl)

    print(eventList[i])
    #ページ取得
    try:
        eventResp = requests.get(eventUrl, timeout=(60))
    except Exception as e:
        traceback.print_exc() 
        print("エラーになったからとばす"+eventUrl)


    eventsoup = BeautifulSoup(eventResp.content, "html.parser")
   


    scheduleTables=eventsoup.find_all('div', attrs={ 'class': ['game_seat_blk'] } )


    for schedule in scheduleTables:
        

        kuusekiImg = schedule.find('div', class_='img').find('img')

        src = kuusekiImg.get('src')

        if 'ico_st1.png' in src:
            print("せきあり")
            iconStr="〇"
            kaijo=eventsoup.find('div', class_='game_place').text.strip().replace('\n', '').replace('\u3000', '').replace(' ', '')
            kouenbi=eventsoup.find('div', class_='game_date1').text.strip().replace('\n', '').replace('\u3000', '').replace(' ', '')
            
            kouenbi=re.search(r'\d{4}[./]\d{1,2}[./]\d{1,2}', kouenbi).group()
            year, month, day = kouenbi.split('.')

            kouenbi = f"{year}/{int(month)}/{int(day)}"


            kouenbi_text = kouenbi.strip()  # 念のため
            # ① 日付部分だけ抽出（例: 2026/01/18）
            m = re.search(r"\d{4}/\d{2}/\d{2}", kouenbi_text)
            if m:
                date_str = m.group()
                kaisai_date = datetime.strptime(date_str, "%Y/%m/%d").date()
                today = date.today()

                # 2日後以前なら continue
                if (kaisai_date - today).days <= daycount:
                    print("開催日がdaycount日後以前のため飛ばす"+kouenbi_text)
                    continue
            
            
            kaien_jikan=eventsoup.find('span', class_='hour_start').text.strip().replace('\n', '').replace('\u3000', '').replace(' ', '')



            seat_div = schedule.find('div', class_='game_seat_status')

            ps = seat_div.find_all('p')

            seat = ps[0].text.strip().replace('\n', '').replace('\u3000', '').replace(' ', '')
            price = ps[1].text.strip().replace('\n', '').replace('\u3000', '').replace(' ', '')

            print(seat, price)

            pull_content=schedule.find('div', class_='pull_content')

            try:
                    #入れ子になってるパターン
                pull_content_details=pull_content.find_all('div', class_='pull_content')

                if not pull_content_details or len(pull_content_details)==0:
                    raise Exception("pull_content 内に 'div.pull_content' が見つかりません")

            

                for pull_content_detail in pull_content_details:
                    status_s=pull_content_detail.find_all('div', class_='game_zone_seat_status')
                    print("入れ子パターン")
                    for status in status_s:
                            


                            status_text=status.text.strip().replace('\n', '').replace('\u3000', '').replace(' ', '')
                            teamName = eventsoup.select_one(".team_name").get_text(strip=True)
                            if "CLUB" not in status_text and "クラブ" not in status_text and "会員" not in status_text and "メンバーシップ" not in status_text  and "CREW" not in status_text :
                                text=teamName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+seat+"///"+price+"///"+eventUrl+"///"+eventName+"///"+status_text
                                print(text)
                                data=data+text+"\n"
                            else :
                                print("対象外"+status_text)




            except Exception as e:
                print("入れ子じゃない")    
                status_s=pull_content.find_all('div', class_='game_seat_status')
                
                for status in status_s:
                        print(status)


                        status_text=status.text.strip().replace('\n', '').replace('\u3000', '').replace(' ', '')
                        teamName = eventsoup.select_one(".team_name").get_text(strip=True)
                        if "CLUB" not in status_text and "クラブ" not in status_text and "会員"  not in status_text and "メンバーシップ" not in status_text  and "CREW" not in status_text :
                            text=teamName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+seat+"///"+price+"///"+eventUrl+"///"+eventName+"///"+status_text
                            print(text)
                            data=data+text+"\n"
                        else :
                            print("対象外"+status_text)













        else:
            ok = False

    


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
