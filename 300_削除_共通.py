from datetime import datetime, timedelta
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



eventKbn = input("削除ファイルの取り込み　処理を選択してください:1=木下大サーカス立川,2=ポップサーカス,3=ハッピードリームサーカス,4=バスケット,5=jleague,6=ローソンプロレス,7=ローソンアイススケート,8=ローソン相撲 ,9=jleague,10=7野球,11=アーティスト,12=ローソン野球,13=木下大サーカス磐田,14=ローソン大学野球2026,15=ラグビー")
if eventKbn=="1" :
    janru="s/111899/d"
    eventNameTittle="木下大サーカス"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'

elif eventKbn=="2":
    janru="s/112283/d"
    eventNameTittle="ポップサーカス"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'

elif eventKbn=="3":
    janru="s/112858/d"
    eventNameTittle="ハッピードリームサーカス"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'

elif eventKbn=="4":
    janru="s/000428"
    eventNameTittle="バスケット"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'

elif eventKbn=="5":
    janru="s/000428"
    eventNameTittle="jleague"
    baseFolder="jleague"
    folder_path_moto= "C:/python/"+baseFolder+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'

elif eventKbn=="6":
    janru=""
    eventNameTittle="プロレス"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
elif eventKbn=="7":
    janru=""
    eventNameTittle="アイススケート"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
elif eventKbn=="8":
    janru="相撲"
    eventNameTittle="相撲"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'

elif eventKbn=="9":
    janru=""
    eventNameTittle="jleague"
    baseFolder="jleague"
    folder_path_moto= "C:/python/"+baseFolder+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'

elif eventKbn=="10":
    janru=""
    eventNameTittle="野球"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'

elif eventKbn=="11":
    janru=""
    eventNameTittle="アーティスト"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
elif eventKbn=="12":
    janru=""
    eventNameTittle="野球"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'

elif eventKbn=="13" :
    janru="s/111899/d"
    eventNameTittle="木下大サーカス_磐田"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
elif eventKbn=="14":
    janru=""
    eventNameTittle="ローソン大学野球2026"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'

elif eventKbn=="15" :
    janru=""
    eventNameTittle="ラグビー"
    baseFolder="ラグビー"
    folder_path_moto= "C:/python/"+baseFolder+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'



else :
    print("その他の入力、終了します。")
    quit()

folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
configfile=folder_path_moto+"/設定/設定ファイル.txt"
configfile_team=folder_path_moto+"/設定/設定_チームリスト.txt"
configfile_team_eigo=folder_path_moto+"/設定/設定_チーム英語リスト.txt"
configfile_ng=folder_path_moto+"/設定/設定_NG席リスト.txt"
configfile_seat=folder_path_moto+"/設定/設定_座席リスト.txt"


filepath_cnt = f"{folder_path}/endcnt_7ticket_"+eventNameTittle+".txt"

# 現在時刻を YYYYMMDD_HHMMSS の形式で取得
now_str = datetime.now().strftime("%Y%m%d_%H%M%S")

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



# ディレクトリとファイル名を分離
directory, filename = os.path.split(filepath)
delete_filename = f"削除_{filename}"
delete_filepath = os.path.join(directory, delete_filename)




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

print("mainGrid =", len(browser.find_elements(By.ID, "mainGrid")))
print("rows =", len(browser.find_elements(By.CSS_SELECTOR, "tr.group.eventRow")))




#html = browser.find_element(By.CSS_SELECTOR, "#mainGrid tbody").get_attribute("innerHTML")
#print(html)

time.sleep(2)  



txtSearch = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID,"search"))
)

if eventKbn=="1" or eventKbn=="2" or eventKbn=="3"or eventKbn=="8":
    txtSearch.send_keys(eventNameTittle)
    time.sleep(2)

if eventKbn=="13" :
    txtSearch.send_keys("木下大サーカス")
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


print(delete_filepath)
lines = []
with open(delete_filepath, "r", encoding="utf-8") as f:
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


      #  targetSheet=seat
    for row in rows:
        try:

            print(row.text)


                #削除済みのものだけ
            # sold = 0 の時だけ check ボタン取得

         

            # 曜日の（〜）を削除


            #clean = kaisaibi.split("（")[0]

            kaisaibi = kaisaibi.replace("（", "(").replace("）", ")")

            # ② '(' で分割して曜日削除
            clean = kaisaibi.split("(")[0]
            # 日付部分を分割
            y, m, d = clean.split("/")

            # 整形
            kaisaibi_text = f"{y}年 {int(m)}月 {int(d)}日"

            print(kaisaibi_text)
            print(jikan)


            eigo_value = team_eigo_dict.get(eventName, eventName)


            timeCheck=False
            match = re.search(r'(\d{1,2}:\d{2})', row.text)
            if match:
                time_str = match.group(1)
                print(time_str)  # → 09:00

            match = re.search(r'(\d{1,2}:\d{2})', jikan)
            if not match:
                print("時間が取得できません")
                continue

            jikan = match.group(1)  # → "09:00"
            t1 = datetime.strptime(time_str, "%H:%M")
            t2 = datetime.strptime(jikan, "%H:%M") 

            # 差分を取得（絶対値）
            diff = abs(t1 - t2)

            if eventKbn=="11":
                if diff <= timedelta(hours=3):
                    timeCheck=True
                    print("OK（3時間以内）")
                else:
                    print("NG（3時間超え）")
            else:            
                if diff <= timedelta(hours=2):
                    timeCheck=True
                    print("OK（2時間以内）")
                else:
                    print("NG（2時間超え）")

            if kaisaibi_text in row.text and timeCheck and (eventName in row.text or eigo_value in row.text):
                
    

                event_id = row.get_attribute("data-eventid")
                multi_selector = f"tr.multi[data-eventlistingslink*='event_id={event_id}']"

                listings =None

                listings = browser.find_elements(By.CSS_SELECTOR, multi_selector)

                if not listings:
                    print("要素が無かった")
                    row.click()
                    try:
                        listings = WebDriverWait(browser, 1).until(
                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, multi_selector))
                        )
                        print("row.click() 後に要素が見つかった")
                       
                    except TimeoutException:
                        print("まだ見つからない → while の最初に戻ってやり直し")
                        # continue すら不要、while True なので勝手に最上部へ戻る
                        pass
                else:
                    print("要素があった")
                    # あったときの処理



                for mini in listings:
                    print(mini.text)
       
                    #シート文字変換パターン
                    values = seat_map.get(sheet)

                    if values is not None:
                        for seatValue in values:
                            if seatValue in mini.text:




                                class_name = mini.get_attribute("class")

                                # checked が無ければクリックしてチェックを入れる
                                if "checked" not in class_name:


                                    btn = mini.find_element(By.CSS_SELECTOR, "td.check.min.pointer.bdrr")

    #                                browser.execute_script("arguments[0].scrollIntoView(true);", btn)
                                    browser.execute_script("arguments[0].click();", btn)

                                    print("clicked")
                                    time.sleep(1)

                    #直接パターン
                    if sheet in mini.text:
                            
                            
                            # soldCol を取得 soldoutは除外
                            sold_text = mini.find_element(By.CSS_SELECTOR, "td.soldCol span").text.strip()

                            print("sold =", sold_text)

                            # 0 以外ならスキップ
                            if sold_text != "0":
                                count=count+1
                                continue
                            
                            class_name = mini.get_attribute("class")

                            # checked が無ければクリックしてチェックを入れる
                            if "checked" not in class_name:
                                btn = mini.find_element(By.CSS_SELECTOR, "td.check.min.pointer.bdrr")

                          #      browser.execute_script("arguments[0].scrollIntoView(true);", btn)
                                browser.execute_script("arguments[0].click();", btn)

                                print("clicked")
                                time.sleep(1)
                         


        except Exception as e:
            print("error:", e)
    count=count+1

print("終了しました")

#プログラムが終了すると勝手に閉じてしまう
time.sleep(1000000)

browser.quit()