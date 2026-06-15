
import ast
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
from selenium.common.exceptions import StaleElementReferenceException
import json
from selenium.webdriver.support.ui import Select
import unicodedata
import re
from datetime import datetime, timedelta
import time

import sys
import os

import pickle

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException  # ← これを追加！


from bs4 import BeautifulSoup

import tkinter as tk


#cookies_file = 'C:/python/brave/morokoshi.pkl'
cookies_file = 'C:/python/chrome/morokoshi.pkl'
now_date = datetime.now().strftime("%Y%m%d")
baseFolder=""
eventKbn = input("流し込み　共通 処理を選択してください:1=木下大サーカス立川,2=ポップサーカス,3=ハッピードリームサーカス,4=バスケット,5=jleague,6=ローソンプロレス,7=ローソン相撲,8=ローソンアイススケート,9=ラグビー,10=7野球,11=アーティスト,12=木下大サーカス磐田,13=ローソン野球 ,14=ローソン6大学野球2026,15=木下大サーカス岡山")
if eventKbn=="1" :
    janru="s/111899/d"
    eventNameTittle="木下大サーカス"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="2":
    janru="s/112283/d"
    eventNameTittle="ポップサーカス"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="3":
    janru="s/112858/d"
    eventNameTittle="ハッピードリームサーカス"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="4":
    janru="s/000428"
    eventNameTittle="バスケット"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="5":
    janru="s/000428"
    eventNameTittle="jleague"
    baseFolder="jleague"
    folder_path_moto= "C:/python/"+baseFolder
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'



    folder_path = "C:/python/"+baseFolder+'/endcnt'
    kanryo_txt='C:/python/'+baseFolder+'/'+'登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+eventNameTittle+".txt"
elif eventKbn=="6":
    janru=""
    eventNameTittle="プロレス"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="7":
    janru=""
    eventNameTittle="相撲"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="8" :
    janru=""
    eventNameTittle="アイススケート"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="9" :
    janru=""
    eventNameTittle="ラグビー"
    baseFolder="ラグビー"
    folder_path_moto= "C:/python/"+baseFolder
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="10":
    janru=""
    eventNameTittle="野球"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"

elif eventKbn=="11":
    janru=""
    eventNameTittle="アーティスト"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="12" :
    janru="s/113193/d"
    eventNameTittle="木下大サーカス_磐田"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="13":
    janru=""
    eventNameTittle="野球"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="14":
    janru=""
    eventNameTittle="ローソン大学野球2026"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
elif eventKbn=="15" :
    janru="s/113193/d"
    eventNameTittle="木下大サーカス_岡山"
    baseFolder="7ticket"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle
    filepath=folder_path_moto+'/7ticket_'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
else :
    print("その他の入力、ローソン大学野球2026にします。")
    janru=""
    eventNameTittle="ローソン大学野球2026"
    baseFolder="lawson"
    folder_path_moto= "C:/python/"+baseFolder+"/"+eventNameTittle+"/"
    filepath=folder_path_moto+'/'+eventNameTittle+'.txt'
    folder_path = "C:/python/"+baseFolder+"/"+eventNameTittle+"/endcnt"
    kanryo_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/登録完了_'+now_date+'_'+eventNameTittle+'.txt'
    filepath_cnt = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"
    #quit()



configfile=folder_path_moto+"/設定/設定ファイル.txt"
configfile_team=folder_path_moto+"/設定/設定_チームリスト.txt"
configfile_team_eigo=folder_path_moto+"/設定/設定_チーム英語リスト.txt"
configfile_ng=folder_path_moto+"/設定/設定_NG席リスト.txt"
configfile_seat=folder_path_moto+"/設定/設定_座席リスト.txt"


os.makedirs(folder_path, exist_ok=True)

filepath_ = f"{folder_path}/endcnt_"+baseFolder+"_"+eventNameTittle+".txt"


# 現在時刻を YYYYMMDD_HHMMSS の形式で取得
now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
sabun_txt='C:/python/'+baseFolder+'/'+eventNameTittle+'/差分_'+now_str+'_'+eventNameTittle+'.txt'





# 現在時刻を YYYYMMDD_HHMMSS の形式で取得
now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
print("configfile:"+configfile)
with open(configfile, "r", encoding="utf-8") as f:
    config = json.load(f)
daycount = config["掲載日数"]
chokusetukeisai=config["直接掲載"]


with open(configfile, "r", encoding="utf-8-sig") as f:
    config = json.load(f)

chokusetukeisai= config["直接掲載"]
daycount = config["掲載日数"]

kakakumoji = config["価格文字"]


shubetu = config["チケット種別"]

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

add_filename = f"追加_{filename}"
add_filepath = os.path.join(directory, add_filename)




shoriKbn = input("追加か全取り込みかどちらですか？:1=追加,2=全取り込み ")


if shoriKbn=="1":
    filepath=add_filepath
    print("追加ファイルで処理:"+filepath)

else:
    print("全取り込みファイルで処理:"+filepath)
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

endCount=0
count=0



if os.path.exists(filepath_cnt):
    with open(filepath_cnt, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        print("1行目:", first_line)
       
        if(first_line==""):
            endCount=0
        else:
            endCount=int(first_line)

else:
    print("ファイルが存在しません:", filepath_cnt)
    endCount=0

hidukenashi_dict = {}

retry_point = False

print(filepath)
lines = []
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()


while count<len(lines):

    
    if(count < endCount ):
        print(str(count)+"は処理済み/"+str(endCount))
        count=count+1
        continue

    if retry_point:
        print("True リトライ中")
        retry_point = False

  
     
        

    try:
        s_line = lines[count].strip()
        print(str(count)+"件目")
        # 処理内容（ここに実際の処理を書く）
        print(f"処理中: {s_line}")

        
            
        data=s_line


        array = data.split("///")

        eventName=array[0]
        english_team=team_eigo_dict[eventName]
        kaijo=array[1]
        kaisaibi=array[2]

        kaisaibi = re.sub(r'\(.+?\)', '', kaisaibi)

      
        m = re.search(r"(\d{4})/(\d{1,2})/(\d{1,2})", kaisaibi)

        if m:
            y, mth, d = m.groups()
            kaisaiFrom = f"{y}/{mth.zfill(2)}/{d.zfill(2)}"

        kaisaiFrom = re.sub(r"\(.*?\)", "", kaisaiFrom)

        if kaisaiFrom is not None:
            kaisaiFrom = re.sub(r"\(.*?\)", "", kaisaiFrom)

        #月と日もセット
        #kaisaiFrom=kaisaidatesplit[0]+"/"+kaisaidatesplit[1].rjust(2, '0')+"/"+kaisaidatesplit[2][:2]
        #kaisai_date = datetime.strptime(kaisaibi, "%Y/%m/%d").date()

        today = date.today()

        kaisaichi=array[1]
        #kaisaichi = re.split(r"[ 　]", kaisaichi)[0]
        kaisaichi = re.split(r"（|[ 　]", kaisaichi)[0]


        if baseFolder=="lawson" :
            kaisaichi = kaisaichi.split("(")[0]
        #町田ＧＩＯＮスタジアムは今のところとばす
        if "町田ＧＩＯＮスタジアム" in kaisaichi:
            print("#町田ＧＩＯＮスタジアムは今のところとばす")
            count=count+1
            with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
                # 文字列をファイルに書き込む
                file.write(str(count))
                file.close
            continue

        if eventKbn=="12" :
            kaisaichi="磐田"
        if eventKbn=="1" : 
            kaisaichi="立川"
            
        jikan=array[3]
        times = []
    
        # 時間フォーマットにマッチする部分を探す（例: 14:00）
        time_strs = re.findall(r'\d{1,2}[:時]\d{2}', jikan)
        times = []
        for t in time_strs:
            t = t.replace("時", ":")
            times.append(datetime.strptime(t, "%H:%M"))

        jikan = max(times).strftime("%H:%M") if times else None

        hidukejikankey = eventName + kaisaiFrom + jikan
        if hidukenashi_dict.get(hidukejikankey) == "1":
            print(hidukejikankey+"はもうないからスルー")

            count=count+1
            with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
                # 文字列をファイルに書き込む
                file.write(str(count))
                file.close


            continue
        #if hidukenashi_dict.get(hidukejikankey) == "1":
        #    print("このチームの日付はもうないのでスルーします " + hidukejikankey)
        #    continue


        jyokyo=array[4]
        data_sheet=array[5]

 

        #  targetSheet=seat_map.get(sheet,"")


        price=array[6]
        price_txt=array[6]
        price = price.strip()
        #if all(x not in price for x in ["共通", "大人", "一般"]) :
        #    print("共通大人一般のみとする。それ以外は一旦スルー:"+price)
        #    continue


        targetSheet = ""

        # 部分一致検索
        for key, value in seat_map.items():
            if key.lower() == data_sheet.lower():  # 大文字小文字を区別せずに検索
                targetSheet = value
                break  # 最初にヒットしたものを採用（複数あるなら調整可）

        # ヒットしなかった場合
        if not targetSheet:
            targetSheet = data_sheet

        if any(ng in data_sheet for ng in ngwords):
            print(data_sheet+"はNGせきなのでスルー")
            count=count+1
            with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
                # 文字列をファイルに書き込む
                file.write(str(count))
                file.close
            continue




        browser.get(SITEURL+KEISAIURL)
        time.sleep(2)   

       # print(browser.page_source)

        #print("newListingをクリック")



        try:
            new_spn_BT = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.ID, "newListing"))
            )
            new_spn_BT.click()
        except TimeoutException:

            # newListing が DOM に現れるまで JS で待つ
            browser.execute_script("""
            const wait = setInterval(() => {
            const icon = document.querySelector('#newListing i.i-plus.mrxs.rel');
            if (icon) {
                clearInterval(wait);
                icon.scrollIntoView({block:'center'});
                icon.click();
            }
            }, 100);
            """)
    
        time.sleep(2)

        try:
            txtSearch = WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.ID,"txtSearch"))
                )
        except TimeoutException:
            print("失敗 → もう一度 while の先頭へ")
            retry_point = True
            continue

        
        browser.execute_script("document.getElementsByClassName('picker__input')[0].removeAttribute('readonly');")
        browser.execute_script("document.getElementsByClassName('picker__input')[1].removeAttribute('readonly');")

        txtSearch.send_keys(eventName)

        kaisaibi = re.sub(r"（.*?）", "", kaisaibi)

        kaisaidatesplit=kaisaibi.split("/")
        print(kaisaibi)
        print(kaisaidatesplit[0])


        #月と日もセット
        kaisaiFrom = (
            kaisaidatesplit[0] + "/" +
            kaisaidatesplit[1].rjust(2, '0') + "/" +
            kaisaidatesplit[2].rjust(2, '0')
        )
        kaisaiFrom_match = (
            kaisaidatesplit[0] + "年 " +
            str(int(kaisaidatesplit[1])) + "月 " +
            str(int(kaisaidatesplit[2])) + "日"
        )

        kaisaidate = datetime(
            int(kaisaidatesplit[0]), 
            int(kaisaidatesplit[1]), 
            int(kaisaidatesplit[2])
        )

        limit_date = datetime.today() + timedelta(days=daycount)

        # もし開催日が今日+daycount 以前ならスキップ
        if kaisaidate <= limit_date:
            print("今日+daycount 以前ならスキップ")
            count=count+1
            continue

        print("check:"+kaisaiFrom)
        dateFrom=browser.find_element(By.ID,"dateFrom")
        #dateFrom.__delattr__("readonly")
        dateFrom.click()
        dateFrom.send_keys(kaisaiFrom)

        

        time.sleep(1)

        
        kaisaiTo=kaisaiFrom
        kaisaiTo_2=kaisaiFrom
        print("kaisaibiTo"+kaisaiTo)

        dateTo=browser.find_element(By.ID,"dateTo")
        #dateTo.__delattr__("readonly")
        dateTo.click()
        dateTo.send_keys(kaisaiTo)

        txtSearch.click()
        txtSearch.send_keys(Keys.ENTER)


        #しばらくまつ　早すぎると無理
        time.sleep(2)

      
        searchDivElem = browser.find_element(By.ID,"searchGrid")

        if searchDivElem is not None:
            ##日程リスト選択
      
            searchGrid=browser.find_element(By.ID,"searchGrid")


            trElems=searchGrid.find_elements(By.CLASS_NAME,"pointer")
            
            if trElems is not None:

                hidukeari=None
                tempElem=None

                i = -1
               

                while True:
                    print(str(i)+"/"+str(len(trElems)))
                    i += 1
                    if i >= len(trElems):
                        break
                    trElem = trElems[i]
                    print("開催地"+kaisaichi)
                    print("trElem.text"+trElem.text)

                    kaisaichitext=trElem.find_element(By.CLASS_NAME,"cGry3").text
                    print("kaisaichitext"+kaisaichitext )

                    def normalize(text):
                        return unicodedata.normalize("NFKC", text)
                    a = normalize(kaisaichitext).strip().replace('\n', '').replace('\u3000', '').replace(' ', '')
                    b = normalize(kaisaichi).strip().replace('\n', '').replace('\u3000', '').replace(' ', '')


                    shorter, longer = (a, b) if len(a) <= len(b) else (b, a)

                    #if (baseFolder!="lawson" and baseFolder!="ラグビー" and baseFolder!="jleague") or shorter in longer:
                    if   shorter in longer:
                        #開催地が一致
                        print("開催地が一致"+kaisaichi)

                        print("kaisaiFrom_match "+kaisaiFrom_match )
                        for trElem in trElems:
                            print("text"+trElem.text)
                            print("kaisaiFrom_match "+kaisaiFrom_match )

                            print(jikan)

                            if kaisaiFrom_match   in trElem.text:

                                print("同じ日付あり")
                                time_elem = trElem.find_element(By.CSS_SELECTOR, "small.bk.cGry4")

                                if time_elem is None:
                                    print("時間表示がない")
                                    hidukeari=trElem
                                                        
                                    
                                else:
                                    # 文字列 → 時刻変換（例: "14:05"）
                                    fmt = "%H:%M"

                                    # 時刻オブジェクト
                                    t1 = datetime.strptime(jikan, fmt)
                                    t2 = datetime.strptime(time_elem.text, fmt)

                                    # 差を絶対値で計算
                                    diff = abs(t1 - t2)

                                    #アーティストは3時間
                                    if eventKbn=="11":
                                        if diff <= timedelta(hours=3, minutes=1):
                                            print(f"時間が±3時間半以内で一致: {jikan} == {time_elem.text}")
                                            hidukeari=trElem
                                            i = len(trElems)
                                        else:
                                            print(f"時間が一致しなかった（±3h半外）{jikan} != {time_elem.text}")
                                        
                                    else:
                                        if diff <= timedelta(hours=2, minutes=15):
                                            print(f"時間が±2時間以内で一致: {jikan} == {time_elem.text}")
                                            hidukeari=trElem
                                            i = len(trElems)
                                        else:
                                            print(f"時間が一致しなかった（±2h外）{jikan} != {time_elem.text}")
                                        
                                    

                            

        #日付が合わない場合 英語で探す
        if hidukeari is None :
            print("同じ日付が見つからなかった英語で探す"+english_team)
        
            txtSearch.clear()  
            txtSearch.send_keys(english_team)
            time.sleep(2)

  
            searchDivElem = browser.find_element(By.ID,"searchGrid")

            if searchDivElem is not None:
                    
                ##日程リスト選択

                searchGrid=browser.find_element(By.ID,"searchGrid")
                trElems=searchGrid.find_elements(By.CLASS_NAME,"pointer")
                i = -1
                while True:
                    i += 1

                    if i >= len(trElems):
                     break
                    trElem = trElems[i]
                    kaisaichitext=trElem.find_element(By.CLASS_NAME,"cGry3").text
                    print("kaisaichitext"+kaisaichitext )
                    def normalize(text):
                        return unicodedata.normalize("NFKC", text)
                    a = normalize(kaisaichitext).strip().replace('\n', '').replace('\u3000', '').replace(' ', '')
                    b = normalize(kaisaichi).strip().replace('\n', '').replace('\u3000', '').replace(' ', '')

                    shorter, longer = (a, b) if len(a) <= len(b) else (b, a)

                    if  shorter in longer:
                                #開催地が一致
                                print("開催地が一致"+kaisaichi)
                                if kaisaiFrom_match   in trElem.text:
                                    
                                    print("同じ日付あり")
                                    time_elem = trElem.find_element(By.CSS_SELECTOR, "small.bk.cGry4")

                                    if time_elem is None:
                                        print("時間表示がない")
                                        hidukeari=trElem
                                                        
                                    
                                    else:
                                        # 文字列 → 時刻変換（例: "14:05"）
                                        fmt = "%H:%M"

                                        # 時刻オブジェクト
                                        t1 = datetime.strptime(jikan, fmt)
                                        print(time_elem.text)
                                        t2 = datetime.strptime(time_elem.text, fmt)

                                        # 差を絶対値で計算
                                        diff = abs(t1 - t2)


                                        #アーティストは3時間
                                        if eventKbn=="11":
                                            if diff <= timedelta(hours=3, minutes=1):
                                                print(f"時間が±3時間半以内で一致: {jikan} == {time_elem.text}")
                                                hidukeari=trElem
                                                i = len(trElems)
                                            else:
                                                print(f"時間が一致しなかった（±3h半外）{jikan} != {time_elem.text}")
                                            
                                        else:
                                            if diff <= timedelta(hours=2, minutes=15):
                                                print(f"時間が±2時間以内で一致: {jikan} == {time_elem.text}")
                                                hidukeari=trElem
                                                i = len(trElems)
                                            else:
                                                print(f"時間が一致しなかった（±2h外）{jikan} != {time_elem.text}")
                                            
                            

                
        #日付が合わない場合
        if hidukeari is None :
            print("同じ日付が見つからなかった hidukenashi_dictに登録します")
            hidukenashi_dict[hidukejikankey] = "1"
            count=count+1
            with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
                # 文字列をファイルに書き込む
                file.write(str(count))
                file.close
            continue


        else:
            print("日付、時刻確認OK")
            hidukeari.click()


        




                
        ##ここで待たないとモーダルの内容がとれない
        time.sleep(2)

        try:
            content_html = WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.ID,"content"))
            )
        except TimeoutException:
            print("失敗 → もう一度 while の先頭へ")
            retry_point = True
            continue
        #print(content_html.text)

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



        if "紙" in shubetu:
            ticket_btn = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.tile.press.mbm.js-select[data-type="PaperTicket"]')
                )
            )
            ticket_btn.click()
        elif "電子" in shubetu:
            ticket_btn = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.tile.press.mbm.js-select[data-type="ETicket"]')
                )
            )
            ticket_btn.click()
        elif "コンビニ" in shubetu:
            ticket_btn = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.tile.press.mbm.js-select[data-type="ReservationWithFaceValue"]')
                )
            )

            ticket_btn.click()
        else:
            continue

        time.sleep(2)
        try:
            content_html = WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.ID,"content"))
            )
        except TimeoutException:
            print("失敗 → もう一度 while の先頭へ")
            retry_point = True
            continue

        try:
            maisuTX = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.XPATH, ".//*[@id='Listing_AvailableTickets']"))
            )
        except TimeoutException:
            print("失敗 → もう一度 while の先頭へ")
            retry_point = True
            continue



        maisuTX.send_keys("2")

        

        
        
        #非掲載
        if chokusetukeisai=="1" or chokusetukeisai==1:
            print("直接掲載")
        else :
            toggle_div = content_html.find_element(By.CLASS_NAME, "toggle")
            label_LB = toggle_div.find_element(By.CSS_SELECTOR, 'label[for="IsPublishToViagogo"]')
            label_LB.click()
        #toggle_div=content_html.find_element(By.CLASS_NAME, "toggle")
        
        #label_LB=toggle_div.find_element(By.TAG_NAME,"label")
        #label_LB.click()
        

        ##ここで待たないとモーダルの内容がとれない
        time.sleep(2)

        
        # section要素を取得して検索語を入力
        SEAT_TXT=""
        try:
            section = content_html.find_element(By.ID, "Listing.Section")

            print("セクション"+section.tag_name)


            print("セクション選択あり。")
            section.send_keys(targetSheet)
            time.sleep(2)  # 候補リストが出るまで少し待つ

            # ▼ 候補リストの中から targetSheet を部分一致で検索
            candidates = content_html.find_elements(By.ID, "Listing.Section")
            matched = None
            for c in candidates:
                # targetSheet が文字列のとき
                if isinstance(targetSheet, str):
                    print("targetSheet"+targetSheet)
                    print("list"+ c.text)
                    for line in c.text.splitlines():
                        if targetSheet.lower() == line.lower():
                            matched = c
                            SEAT_TXT = line   # 一致した行だけ
                            break
                        if matched:
                            break


                # targetSheet がリストのとき（例: ["S指定席", "s seat"]）
                elif isinstance(targetSheet, list):

                    def norm(s):
                        return unicodedata.normalize("NFKC", s)

                    for sheet_ in targetSheet:
                        print("targetSheet"+sheet_)
                        print("list"+ c.text)
                        for line in c.text.splitlines():
                            if norm(sheet_).lower() == norm(line).lower():
                                matched = c
                                SEAT_TXT = line   # 一致した行だけ
                                break
                            if matched:
                                break
                    if matched:
                        break

            # すべての候補をチェックしたあとで結果を判定
            if matched:
                print("matched"+ SEAT_TXT)
                selection = content_html.find_element(By.ID, "Listing.Section")
                sel = Select(selection)

                # matched.text から「ひとつ選択して下さい…」行を除いてクリーン化
                
                #print("matched lines:", SEAT_TXT)      
                # 「Reserved Seating」だけを抽出（1行しかないならそのまま）
                clean_text = SEAT_TXT

                #Reserved Seatingの時だけうまくいかないから制御
                if "ひとつ選択して下さい…\n" in SEAT_TXT:
                    raw_lines = [line.strip() for line in SEAT_TXT.splitlines() if line.strip()]
                    for line in raw_lines:
                        if "ひとつ選択" not in line and "select" not in line.lower():
                            clean_text = re.sub(r'\s+', ' ', line).strip()
                            break

                print(f"[DEBUG] clean_text = '{clean_text}'")

                # ▼ Selectで選択
                try:
                    sel.select_by_visible_text(clean_text)
                    print(f"✅ '{clean_text}' を選択しました。")
                except Exception as e:
                    print(f"⚠ '{clean_text}' の選択に失敗しました: {e}")

                # ▼ hidden inputの反映を確認
                time.sleep(2)
                hidden_input = content_html.find_element(By.ID, "Listing_Section")
                print("Hidden input 現在値:", hidden_input.get_attribute("value"))
            else:
                # 候補がなかった場合、キャンセルボタンをクリック

                print("候補がなかったためスキップしました:"+data_sheet)
                cancel_btn = content_html.find_element(By.CSS_SELECTOR, ".btn.sec.modal-close")
                cancel_btn.click()
               
                count=count+1
                with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
                    # 文字列をファイルに書き込む
                    file.write(str(count))
                    file.close

                continue

        except NoSuchElementException:
            # なければinputを取得
            section = content_html.find_element(By.ID, "Listing_Section")
            print("セクション"+section.tag_name)
            print("inputタグを取得:", section.tag_name)
            section = None
            print("セクション選択なし直接入力。"+data_sheet)
            section = content_html.find_element(By.CLASS_NAME, "js-section-text")
            section.send_keys(data_sheet)
                
        if kakakumoji=="max":
            prices = [int(p.replace(",", "")) for p in re.findall(r'\d[\d,]*', price_txt)]
            max_price = max(prices)
        else:
            match = re.search(
                rf"{kakakumoji}.*?(\d[\d,]*)円",
                price_txt
            )
            if match:
                print(kakakumoji+"料金:", match.group(0))
                print("金額部分:", match.group(1))  # 数字だけ
                max_price=int(match.group(1).replace(",", ""))
            else:
                print(kakakumoji+"料金が見つかりませんでした")
                count=count+1
                with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
                    # 文字列をファイルに書き込む
                    file.write(str(count))
                    file.close
                    continue

        if ('スタンド' in data_sheet or 'スタンディング' in data_sheet) and 'スタンド椅子' not in data_sheet:
            
            try:
                standBtns=browser.find_elements(By.CSS_SELECTOR,".js-is-seated-btn")

                for standBtn in standBtns:
                    #classes = standBtn.get_attribute("class")
                    print(standBtn.text)
                    if "スタンディング"  in standBtn.text:
                        standBtn.click()
            except Exception as e:
                print("スタンディング選択なし？")

      

        price_int=int(max_price)
        print(price_int) 

        price_int=price_int+2500

        elements = browser.find_elements(By.XPATH, "//input[@name='Listing.PostUploadReservation' and @value='True']")
        if elements:
            elements[0].click()

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



        time.sleep(2)




        btnOk = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn.mtxs.js-ok.pri.mbm"))
        )
        btnOk.click()
                

        with open(kanryo_txt, "a", encoding="utf-8") as f:
            f.write(s_line + "\r\n")


        count=count+1
        with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
            # 文字列をファイルに書き込む
            file.write(str(count))
            file.close


        continue

    except Exception as e:
            print("エラーが発生 → もう一度 while の先頭へ"+str(e))
            traceback.print_exc() 
            browser.get(SITEURL+KEISAIURL)
            time.sleep(2) 
            retry_point = True
            continue

   

print("登録終了しました")

#   browser.execute_script("arguments[1].click();", uploadCheck)

#プログラムが終了すると勝手に閉じてしまう
time.sleep(1000000)

browser.quit()