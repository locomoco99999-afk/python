from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options

import time

import sys
import os

import pickle


import datetime

from bs4 import BeautifulSoup

import tkinter as tk


#cookies_file = 'C:/python/brave/morokoshi.pkl'
cookies_file = 'C:/python/chrome/morokoshi.pkl'


janru="sports-baseball-.txt"
filepath='C:/python/piaweb/'+janru

listFilepath="C:/python/piaweb/list-sports-baseball-.txt"
##artistListFilepath="C:/python/piaweb/artist_list.txt"

sheetFilepath="C:\python\piaweb\sheet-sports-baseball-.txt"

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

#profile_path="C:/Users/locom/AppData/Local/Temp/scoped_dir26368_938757101/Default"

#option.add_argument('--user-data-dir=' + profile_path)
#option.add_argument('--profile-directory=Default')



browser.get(SITEURL)

time.sleep(6000000)

#loginTX = browser.find_element(By.ID,'Login_UserName')
#loginTX.send_keys(ID)

#passwordTX=browser.find_element(By.ID,"Login_Password")
#passwordTX.send_keys(PASSWORD)

#loginBT=browser.find_element(By.ID,"sbmt")
#loginBT.click()




#browser.get(SITEURL+KEISAIURL)

#new_spn_BT=browser.find_element(By.ID,"newListing")
#new_spn_BT.click()



#if os.path.exists(cookies_file):
#    cookies = pickle.load(open(cookies_file,'rb')) 

#    for c in cookies: # クッキーを設定する
#        if c["domain"] == "viagogo.com":
#            browser.add_cookie(c)
#    browser.get(SITEURL)

#else:
#    cookies = browser.get_cookies() 
#    pickle.dump(cookies,open(cookies_file,'wb'))


