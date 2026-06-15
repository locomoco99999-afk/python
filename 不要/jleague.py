import requests
from datetime import datetime, date
import time
from bs4 import BeautifulSoup
import os
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#cookies_file = 'C:/python/brave/morokoshi.pkl'
cookies_file = 'C:/python/chrome/morokoshi.pkl'

filepath = "C:/python/jleague/jleague.txt"


option = webdriver.ChromeOptions()
option.debugger_address = "127.0.0.1:9222"

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




# 現在時刻を YYYYMMDD_HHMMSS の形式で取得
now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
sabun_txt='C:/python/jleague/'+now_str+'_sabun_jleague.txt'



before_filename=""
before_filepath=""


add_filename=""
add_filepath=""
delete_filename=""
delete_filepath=""




BASE_URL = "https://www.jleague-ticket.jp/"

data=""

team_lists = [
    ["鹿島アントラーズ", "club/ka"],
    ["浦和レッズ", "club/ur"],
    ["柏レイソル", "club/kr"],
    ["ＦＣ東京", "club/to"],
    ["東京ヴェルディ", "club/vn"],
    ["ＦＣ町田ゼルビア", "club/mz"],
    ["川崎フロンターレ", "club/kf"],
    ["横浜Ｆ・マリノス", "club/ym"],
    ["横浜ＦＣ", "club/yk"],
    ["湘南ベルマーレ", "club/bm"],
    ["アルビレックス新潟", "club/an"],
    ["清水エスパルス", "club/ss"],
    ["名古屋グランパス", "club/ng"],
    ["京都サンガＦ.Ｃ.", "club/ks"],
    ["ガンバ大阪", "club/go"],
    ["セレッソ大阪", "club/co"],
    ["ヴィッセル神戸", "club/vi"],
    ["ファジアーノ岡山", "club/fo"],
    ["サンフレッチェ広島", "club/sh"],
    ["アビスパ福岡", "club/af"],
     ["北海道コンサドーレ札幌", "club/cs"],
    ["ベガルタ仙台", "club/vs"],
    ["ブラウブリッツ秋田", "club/ba"],
    ["モンテディオ山形", "club/my"],
    ["いわきFC", "club/iw"],
    ["水戸ホーリーホック", "club/mh"],
    ["大宮アルディージャ", "club/oa"],
    ["ジェフユナイテッド千葉", "club/je"],
    ["ヴァンフォーレ甲府", "club/ve"],
    ["カターレ富山", "club/kt"],
    ["ジュビロ磐田", "club/ju"],
    ["藤枝MYFC", "club/fj"],
    ["レノファ山口FC", "club/ry"],
    ["徳島ヴォルティス", "club/vo"],
    ["愛媛FC", "club/eh"],
    ["FC今治", "club/fi"],
    ["サガン鳥栖", "club/st"],
    ["V・ファーレン長崎", "club/vv"],
    ["ロアッソ熊本", "club/rk"],
    ["大分トリニータ", "club/ot"],
    ["ヴァンラーレ八戸", "club/vh"],
    ["福島ユナイテッドFC", "club/fu"],
    ["栃木SC", "club/ts"],
    ["栃木シティFC", "club/tc"],
    ["ザスパ群馬", "club/pa"],
    ["SC相模原", "club/sg"],
    ["松本山雅FC", "club/yg"],
    ["AC長野パルセイロ", "club/np"],
    ["ツエーゲン金沢", "club/zk"],
    ["アスルクラロ沼津", "club/ac"],
    ["FC岐阜", "club/fg"],
    ["FC大阪", "club/os"],
    ["奈良クラブ", "club/nc"],
    ["ガイナーレ鳥取", "club/gt"],
    ["カマタマーレ讃岐", "club/km"],
    ["高知ユナイテッドSC", "club/kc"],
    ["ギラヴァンツ北九州", "club/gv"],
    ["テゲバジャーロ宮崎", "club/tm"],
    ["鹿児島ユナイテッドFC", "club/ku"],
    ["FC琉球", "club/fr"]
]

    

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
    response = requests.get(TARGET_URL)


    #タグを整形
    soup = BeautifulSoup(response.content, "html.parser")

    li_tags = []

    game_lists = soup.find_all("div", class_="game-list")

    for gl in game_lists:
       
        #print(gl.prettify())
        ul = gl.find("ul")
        if not ul:
            continue
        for li in ul.find_all("li"):  # ←これが一番確実
            #print(li.text)
            li_tags.append(li)
            print(len(li_tags))
    for get_li in li_tags:
        place_div = get_li.find("div", class_="vs-box")
        if not place_div:
            continue

        place_text = place_div.get_text(" ", strip=True)
        if "box" in place_text:
            continue
        if "駐車券" in place_text:
            continue

        status_div = get_li.find("div", class_="comp-status")
    
        if status_div:
            status_text = status_div.get_text(strip=True)

            if status_text == "空席あり":

                # チケット購入の <span> を取得
                span = get_li.find("span", class_="ticket-status")
                
                if span and span.has_attr("href"):
                    link = span["href"]
         
                    kobetu_url=BASE_URL+link
                    response2 = requests.get(kobetu_url)
                    soup2 = BeautifulSoup(response2.content, "html.parser")

                    #公演タイトル
                    h3 = soup2.find("h3", class_="game-info-ttl")
                    if h3:
                        kaijo = h3.get_text(strip=True)
                        print(kaijo)

                    #公演日
                    hiduke_div = soup2.find("div", class_="game-info")
                    kouenbi= hiduke_div.find_all("span",class_="day")[0].text
                    kaien_jikan= hiduke_div.find_all("span",class_="day")[1].text

   
                    kaisai_date = datetime.strptime(kouenbi, "%Y/%m/%d").date()
                    today = date.today()

                    # 2日後以前なら continue
                    if (kaisai_date - today).days <= 2:
                        print("開催日が2日後以前のため飛ばす"+kouenbi)
                        continue

                   # div.seat-select-list の中の dl を取得
                    seat_list_divs = soup2.find_all("div", class_="seat-select-list")
                   
                    for seat_div in seat_list_divs:
                        dls = seat_div.find_all("dl")  # div の中の dl を取得
                        for dl in dls:
                            seat_status_div = dl.find("div", class_=["seat-select-list-img"])
                            if seat_status_div:
                                #print("空席があります")

                                seat_name_div = dl.find("div", class_=["seat-select-list-txt"])

                                print(seat_name_div.text)

                                if seat_name_div:
                                    h4 = seat_name_div.find("h4")
                                    if h4:
                                        seat_name = h4.get_text(strip=True)

                                        if "リセール" in seat_name:
                                            continue

                                else:
                                    continue
                                       
                                #チケット種類　空席あり
                                dd = dl.find("dd")
                                if dd:
                                    #print(dd.prettify())
                                    seat_status_list = dl.find_all("li")

                                    for seat_status_row in seat_status_list:
                                        seat_kaind_div = seat_status_row.find("div", class_=["list-items-cts-desc"])
                                        seat_kaind_txt= seat_status_row.find("div", class_=["list-items-cts-desc"]).text

                                        img = dl.find("img")
                                        img_icon_txt = img.get("src")   # → "/img/ico_no2.png"
                                        if "vacant2.png" in img_icon_txt:
                                            print("せきあり")
                                        else :
                                            continue

                                        typeStr=dl.find("div", class_="seat-select-list-txt").find("h4").text
                                        if "ＱＲ" in seat_kaind_txt and not ("ファンクラブ" in seat_kaind_txt or "CLUB" in seat_kaind_txt or "ＣＬＵＢ" in seat_kaind_txt):

                                            
                                            img2 = dd.find("img")
                                            img_icon_txt2 = img2.get("src")   # → "/img/ico_no2.png"
                                            if "vacant2.png" in img_icon_txt:
                                                print("チケットせきあり")
                                            else :
                                                continue

                                            priceStr=seat_kaind_div.find("p").text.split("/", 1)[0]
                                            if priceStr=="0円":
                                             continue
                                            text=eventName+"///"+kaijo+"///"+kouenbi+"///"+kaien_jikan+"///"+iconStr+"///"+typeStr+"///"+priceStr+"///"+kobetu_url
                                            data=data+text+"\n"
                            else:
                                #print("空席はありません")
                                continue





# ファイルが存在しているかチェック
if os.path.exists(filepath):
  
    # ディレクトリとファイル名を分離
    directory, filename = os.path.split(filepath)

    # 新しいファイル名を作成
    before_filename = f"{now_str}_{filename}"
    before_filepath = os.path.join(directory, before_filename)

    add_filename = f"add_{filename}"
    add_filepath = os.path.join(directory, add_filename)

    delete_filename = f"delete_{filename}"
    delete_filepath = os.path.join(directory, delete_filename)


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
        f.write("")


