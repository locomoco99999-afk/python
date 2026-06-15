import traceback
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


janru="g-000428.txt"
filepath="C:\python\jleague\jleague.txt"


folder_path = "C:/python/jleague/endcnt"
os.makedirs(folder_path, exist_ok=True)
#today = datetime.now().strftime("%Y%m%d")
filepath_cnt = f"{folder_path}/endcnt_jleague.txt"




#座席の紐づけマップ
seat_map = {
    "Ｓ指定席ロアー": ["Ｓ指定席ロアー","Ｓ指定席","S Reserve lower","S lower"],
    "Ｓ指定席アッパー": ["Ｓ指定席アッパー","Ｓ指定席","S Reserve Upper","S Upper"],
    "レッズシート": ["レッズシート"],
    "ＳＡメイン北指定席": ["SA指定席"],
    "ＳＡバック指定席": ["SA指定席"], 
    "ＳＡメイン南指定席": ["SA指定席","SA Reserve","SA seat"], 
    "ＳＢ指定席": ["SB指定席","SB Reserve","SB seat"], 
    "ウェルカムシート": ["Welcome Seat"], 
    "ビジター指定席": ["ビジター指定席"], 
    "ビジター自由席": ["ビジター自由席"], 
    "メインＳＳＳ": ["メインＳＳＳ"], 
    "メインＳＳ": ["メインＳＳ"], 
    "メインＳ": ["メインS"], 
    "プレミアムシート": ["プレミアムシート"], 
    "ヴィッセルシート": ["ヴィッセルシート"], 
    "デラックスシート": ["デラックスシート"], 
    "【最前列】メイン特別指定": ["メイン特別指定"], 
    "【最前列】メイン中央指定": ["メイン中央指定"], 
    
 "アウェイゴール": ["アウェイゴール"], 
 "エキサイティングシート前方": ["エキサイティングシート"], 
 "エキサイティングシート": ["エキサイティングシート"], 
 "ホームメイン北SS指定席前方": ["ホームメインSS"], 
 "ホームメイン南SS指定席前方": ["ホームメインSS"], 
 
 "ホームメイン北S指定席前方": ["ホームメインS"], 
 "ホームメイン南S指定席前方": ["ホームメインS"], 
 "バックセンターシート下段ホーム": ["バックセンター"], 

 "【最前列】メイン中央指定": ["メイン指定","main reserve"], 
"【最前列】メイン前段指定": ["メイン指定","main reserve"], 
 "アビスパシート指定": ["アビスパシート"], 

 "メインスタンド自由（Ｍ１）": ["メインスタンド自由"], 
 "メインスタンド指定（Ｍ１）": ["メインスタンド指定"], 
 "アビスパシート指定": ["アビスパシート"], 
 "アビスパシート指定": ["アビスパシート"], 
 "ピッチサイドシート指定（Ｂ２）": ["ピッチサイドシート"], 
 "バックホーム自由": ["back home","バックホーム自由"], 
 

 "メインアッパー指定席": ["メインアッパー 指定席","メインアッパー指定席"],
 "メインアッパー 指定席": ["メインアッパー 指定席","メインアッパー指定席"],

 "バックアッパー指定席": ["バックアッパー 指定席","バックアッパー指定席"],
 "バックアッパー 指定席": ["バックアッパー 指定席","バックアッパー指定席"],
 
 "メインアッパー自由席": ["メインアッパー 自由席","メインアッパー自由席"],
 "メインアッパー 自由席": ["メインアッパー 自由席","メインアッパー自由席"],

 "バックアッパー自由席": ["バックアッパー 自由席","バックアッパー自由席"],
 "バックアッパー 自由席": ["バックアッパー 自由席","バックアッパー自由席"],

 "ゴール裏指定席１階北側": ["1st Floor Reserved Seats Behind The Goal - North"],
 "ゴール裏指定席２階北側": ["2nd Floor Reserved Seats Behind The Goal - North"],
 

 "ゴール裏指定席１階南側": ["1st Floor Reserved Seats Behind The Goal - South"], 
 "ゴール裏指定席２階南側": ["2nd Floor Reserved Seats Behind The Goal - South"], 


 "ビッグ上段指定席": ["ビッグ上段指定席","ビッグ上段指定席"],

 "ホーム自由": ["ホーム自由","ホーム自由席"],
 "W2指定席": ["W2指定席"],
 "E1センター指定席": ["E1センター指定席"],
 "バックセンターＵＦ": ["バックセンターＵＦ"],


 "ミックスメイン南S指定席": ["ミックスメイン南S指定席","ミックスメイン南指定席S"],

 "ホームサポーター自由席": ["ホームサポーター自由席","ホームサボータ一自由席","ホームサボータ一自由席"],
 "ホームサポーター指定席": ["ホームサポーター指定席","ホームサポーター指定席","ホームサボータ一指定席"],

 "ビジターサポーター自由席": ["ビジターサポーター自由席","ビジターサボーター自由席","ビジターサボータ一自由席"],
 "ビジターサポーター指定席": ["ビジターサポーター指定席","ビジターサボーター指定席","ビジターサボーター指定席"],

 "アウェイ指定席": ["アウェイ指定席","away reserve"],
"ホーム指定席": ["ホーム指定席","home reserve"]



}

ngwords = [
    "定員",
    "車イス",
    "車椅子",
    "ペア",
    "ファミリー",
    "キングシート",
    "クイーンシート",
    "プリンス",
    "カウンター",
    "グループシート",
    "グループ",
    "ユニバーサル席",
    "条件付",
    "2名",
    "4名",
    "6名",
    "8名",
    "介助者",
    "お土産",
    "セブン-イレブン",
    "セブンイレブン",
    "テーブル",
    "ベビー",
    "注釈付",
    "ラウンジ",
    "BOX",
    "ボックス",
    "パーティー",
    "PARTY",
    "病院",
    "駐車場",
    "駐車券" ,
    "ブランケット",
   "ユニバーサル席"
]
team_eigo_dict = {
    # --- J1 ---
    "鹿島アントラーズ": "Kashima Antlers",
    "浦和レッズ": "Urawa Red Diamonds",
    "柏レイソル": "Kashiwa Reysol",
    "ＦＣ東京": "FC Tokyo",
    "東京ヴェルディ": "Tokyo Verdy",
    "ＦＣ町田ゼルビア": "FC Machida Zelvia",
    "川崎フロンターレ": "Kawasaki Frontale",
    "横浜Ｆ・マリノス": "Yokohama F. Marinos",
    "横浜ＦＣ": "Yokohama FC",
    "湘南ベルマーレ": "Shonan Bellmare",
    "アルビレックス新潟": "Albirex Niigata",
    "清水エスパルス": "Shimizu S-Pulse",
    "名古屋グランパス": "Nagoya Grampus",
    "京都サンガＦ.Ｃ.": "Kyoto Sanga FC",
    "ガンバ大阪": "Gamba Osaka",
    "セレッソ大阪": "Cerezo Osaka",
    "ヴィッセル神戸": "Vissel Kobe",
    "ファジアーノ岡山": "Fagiano Okayama",
    "サンフレッチェ広島": "Sanfrecce Hiroshima",
    "アビスパ福岡": "Avispa Fukuoka",

    # --- J2 ---
    "北海道コンサドーレ札幌": "Hokkaido Consadole Sapporo",
    "ベガルタ仙台": "Vegalta Sendai",
    "ブラウブリッツ秋田": "Blaublitz Akita",
    "モンテディオ山形": "Montedio Yamagata",
    "いわきＦＣ": "Iwaki FC",
    "水戸ホーリーホック": "Mito Hollyhock",
    "大宮アルディージャ": "Omiya Ardija",
    "ジェフユナイテッド千葉": "JEF United Chiba",
    "ヴァンフォーレ甲府": "Ventforet Kofu",
    "カターレ富山": "Kataller Toyama",
    "ジュビロ磐田": "Jubilo Iwata",
    "藤枝ＭＹＦＣ": "Fujieda MYFC",
    "レノファ山口ＦＣ": "Renofa Yamaguchi FC",
    "徳島ヴォルティス": "Tokushima Vortis",
    "愛媛ＦＣ": "Ehime FC",
    "ＦＣ今治": "FC Imabari",
    "サガン鳥栖": "Sagan Tosu",
    "Ｖ・ファーレン長崎": "V-Varen Nagasaki",
    "ロアッソ熊本": "Roasso Kumamoto",
    "大分トリニータ": "Oita Trinita",

    # --- J3 ---
    "ヴァンラーレ八戸": "Vanraure Hachinohe",
    "福島ユナイテッドＦＣ": "Fukushima United FC",
    "栃木ＳＣ": "Tochigi SC",
    "栃木シティＦＣ": "Tochigi City FC",
    "ザスパ群馬": "Thespakusatsu Gunma",
    "ＳＣ相模原": "SC Sagamihara",
    "松本山雅ＦＣ": "Matsumoto Yamaga FC",
    "ＡＣ長野パルセイロ": "AC Nagano Parceiro",
    "ツエーゲン金沢": "Zweigen Kanazawa",
    "アスルクラロ沼津": "Azul Claro Numazu",
    "FC岐阜": "FC Gifu",
    "FC大阪": "FC Osaka",
    "ＦＣ岐阜": "FC Gifu",
    "ＦＣ大阪": "FC Osaka",
    "奈良クラブ": "Nara Club",
    "ガイナーレ鳥取": "Gainare Tottori",
    "カマタマーレ讃岐": "Kamatamare Sanuki",
    "高知ユナイテッドＳＣ": "Kochi United SC",
    "ギラヴァンツ北九州": "Giravanz Kitakyushu",
    "テゲバジャーロ宮崎": "Tegevajaro Miyazaki",
    "鹿児島ユナイテッドＦＣ": "Kagoshima United FC",
    "FC琉球": "FC Ryukyu",
    "ＦＣ琉球": "FC Ryukyu"
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

        line = s_line.strip()
       
        with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
            # 文字列をファイルに書き込む
            file.write(str(count))
            file.close

        # 処理内容（ここに実際の処理を書く）
        print(f"処理中: {line}")

      
            
        data=s_line


        array = data.split("///")

        eventName=array[0]
        english_team=team_eigo_dict[eventName]
        kaijo=array[1]
        kaisaibi=array[2]
        kaisai_date = datetime.strptime(kaisaibi, "%Y/%m/%d").date()

        today = date.today()

        # 2日後以前なら continue
        if (kaisai_date - today).days <= 2:
            print("開催日が2日後以前のため飛ばす")
            continue


        
        jikan=array[3]


        hidukejikankey = eventName + kaisaibi + jikan
        if hidukenashi_dict.get(hidukejikankey) == "1":
            print("このチームの日付はもうないのでスルーします " + hidukejikankey)
            continue


        jyokyo=array[4]
        sheet=array[5]
      #  targetSheet=seat_map.get(sheet,"")


        price=array[6]
        price = price.strip()
        #if all(x not in price for x in ["共通", "大人", "一般"]) :
        #    print("共通大人一般のみとする。それ以外は一旦スルー:"+price)
        #    continue


        targetSheet = ""

        # 部分一致検索
        for key, value in seat_map.items():
            if key.lower() in sheet.lower():  # 大文字小文字を区別せずに検索
                targetSheet = value
                break  # 最初にヒットしたものを採用（複数あるなら調整可）

        # ヒットしなかった場合
        if not targetSheet:
            targetSheet = sheet

        if any(ng in sheet for ng in ngwords):
            print(sheet+"はNGせきなのでスルー")
            count=count+1
            with open(filepath_cnt, 'w+',encoding='UTF-8') as file:
                # 文字列をファイルに書き込む
                file.write(str(count))
                file.close
            continue




        browser.get(SITEURL+KEISAIURL)
        time.sleep(2)   
        new_spn_BT = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "newListing"))
        )

   
        new_spn_BT.click()
        time.sleep(2)
        txtSearch = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID,"txtSearch"))
        )
      
        browser.execute_script("document.getElementsByClassName('picker__input')[0].removeAttribute('readonly');")
        browser.execute_script("document.getElementsByClassName('picker__input')[1].removeAttribute('readonly');")

        txtSearch.send_keys(eventName)


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
        time.sleep(2)
        
        searchDivElem = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.ID, "searchGrid"))
        )

        ##日程リスト選択
        trElems = searchDivElem.find_elements(By.CLASS_NAME, "pointer")

        hidukeari=None
        tempElem=None

        print("kaisaiFrom_2"+kaisaiFrom_2)
        for trElem in trElems:
            print("text"+trElem.text)
            print("kaisaiFrom_2"+kaisaiFrom_2)

            if kaisaiFrom_2  in trElem.text:
                hidukeari=trElem
                print("同じ日付あり")
                break
        

        #日付が合わない場合 英語で探す
        if hidukeari is None :
             print("同じ日付が見つからなかった英語で探す"+english_team)
         
             txtSearch.clear()  
             txtSearch.send_keys(english_team)
             time.sleep(2)
             trElems = WebDriverWait(browser, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,"pointer"))
             )
              
             for trElem in trElems:
                print("text"+trElem.text)


                if kaisaiFrom_2  in trElem.text:
                    hidukeari=trElem
                    print("同じ日付あり")
                



            


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
            hidukeari.click()


     




             
  ##ここで待たないとモーダルの内容がとれない
        time.sleep(2)

        content_html = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.ID,"content"))
        )
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


        ticket_btn = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.tile.press.mbm.js-select[data-type="ETicket"]')
            )
        )
        ticket_btn.click()


        time.sleep(2)
        content_html = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.ID,"content"))
        )


        maisuTX = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, ".//*[@id='Listing_AvailableTickets']"))
        )


        maisuTX.send_keys("2")

        

        
        
        #非掲載
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

                    for sheet in targetSheet:
                        print("targetSheet"+sheet)
                        print("list"+ c.text)
                        for line in c.text.splitlines():
                            if norm(sheet).lower() == norm(line).lower():
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
                cancel_btn = content_html.find_element(By.CSS_SELECTOR, ".btn.sec.modal-close")
                cancel_btn.click()
                print("候補が見つからず、キャンセルボタンを押しました。:" + str(targetSheet))
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
            print("セクション選択なし直接入力。"+sheet)
            section = content_html.find_element(By.CLASS_NAME, "js-section-text")
            section.send_keys(sheet)
                
         
        m = re.search(r'～(\d+)円', price)
        if "～" in price:
            # ～ がある → 右側の金額を取得
            m = re.search(r'～(\d+)円', price)
            price_int = int(m.group(1))
        else:
            # ～ がない → 最初の金額を取得
            m = re.search(r'(\d+)円', price)
            price_int = int(m.group(1))


        print(price_int) 

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


        time.sleep(2)

        btnOk = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn.mtxs.js-ok.pri.mbm"))
        )
        btnOk.click()
                

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