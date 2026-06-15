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

print("mainGrid =", len(browser.find_elements(By.ID, "mainGrid")))
print("rows =", len(browser.find_elements(By.CSS_SELECTOR, "tr.group.eventRow")))

iframes = browser.find_elements(By.TAG_NAME, "iframe")
print("iframe count =", len(iframes))


html = browser.find_element(By.CSS_SELECTOR, "#mainGrid tbody").get_attribute("innerHTML")
print(html)

time.sleep(1)  


rows = WebDriverWait(browser, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.group.eventRow"))
)


print(len(rows))
count=0
rows = WebDriverWait(browser, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.group.eventRow"))
)

print("row count =", len(rows))

for row in rows:
    row.click()
   


time.sleep(5)     
rows = browser.find_elements(By.CSS_SELECTOR, "tr.multi")

print("行数:", len(rows))

for row in rows:
    try:
        # soldCol を取得
        sold_text = row.find_element(By.CSS_SELECTOR, "td.soldCol span").text.strip()

        print("sold =", sold_text)

        # 0 以外ならスキップ
        if sold_text != "0":
            continue

        # sold = 0 の時だけ check ボタン取得
        btn = row.find_element(By.CSS_SELECTOR, "td.check.min.pointer.bdrr")

        browser.execute_script("arguments[0].scrollIntoView(true);", btn)
        browser.execute_script("arguments[0].click();", btn)

        print("clicked")

    except Exception as e:
        print("error:", e)


#プログラムが終了すると勝手に閉じてしまう
time.sleep(1000000)

browser.quit()