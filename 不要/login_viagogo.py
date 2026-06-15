from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options

import time

import sys
import os

import pickle

from twocaptcha import TwoCaptcha

import datetime


cookies_file = 'C:/python/brave/morokoshi.pkl'
#cookies_file = 'C:/python/chrome/morokoshi.pkl'

filepath='C:/python/piaweb/hgk.txt'
artistListFilepath="C:/python/piaweb/artist_list.txt"

option = webdriver.ChromeOptions()
# Brave本体が、保存されているパスを入力
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'  # Windowsの場合
#option.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  # Windowsの場合



# WebDriverを保存したファイルパスを入力
driver_path = 'C:/python/brave/chromedriver.exe'  # パスを書き換えて下さい
#driver_path = 'C:/python/chrome/chromedriver.exe'  # パスを書き換えて下さい

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')


SITEURL="https://inv.viagogo.com"
#SITEURL="https://www.yahoo.co.jp/"
KEISAIURL="/Listings"

ID="herrkagami@gmail.com"
PASSWORD="2942Tiger"

SERVICE_KEY =""
#SITEKEY='6LcnF3snAAAAAC0UQfNtqE2lUKxcPrNgPBzvPT7q'

#chrome://version

service = fs.Service(executable_path=driver_path)

browser = webdriver.Chrome(options=option, service=service)

#profile_path="C:/Users/locom/AppData/Local/Temp/scoped_dir26368_938757101/Default"

#option.add_argument('--user-data-dir=' + profile_path)
option.add_argument('--profile-directory=Default')



browser.get(SITEURL)

time.sleep(3)

loginTX = browser.find_element(By.ID,'Login_UserName')
loginTX.send_keys(ID)

passwordTX=browser.find_element(By.ID,"Login_Password")
passwordTX.send_keys(PASSWORD)

#loginBT=webd.find_element(By.ID,"sbmt")
#loginBT.click()


time.sleep(80)

print("待機終了")

browser.get(SITEURL+KEISAIURL)

new_spn_BT=browser.find_element(By.ID,"newListing")
new_spn_BT.click()


time.sleep(2)

#if os.path.exists(cookies_file):
#    cookies = pickle.load(open(cookies_file,'rb')) 

#    for c in cookies: # クッキーを設定する
#        if c["domain"] == "viagogo.com":
#            browser.add_cookie(c)
#    browser.get(SITEURL)

#else:
#    cookies = browser.get_cookies() 
#    pickle.dump(cookies,open(cookies_file,'wb'))


time.sleep(5)


data=""
count=0
##一旦一番最初のデータのみとする
with open(filepath, encoding="utf-8") as f:
    for s_line in f:

        #一旦最初のみ
        if count>0:
            break
        count=count+1
            
        data=s_line


        array = data.split("///")

        artistAndTittle=array[0].replace("★","").replace("■","")



        artist=""
        with open(artistListFilepath, encoding="utf-8") as f:
            for s_line in f:
                print(artistAndTittle)
                print(s_line)
                s_line=s_line.replace("\n","")
                if artistAndTittle.find(s_line)>0 :
                   artist=s_line
                   break

        if artist=="" :
            continue


        browser.execute_script("document.getElementsByClassName('picker__input')[0].removeAttribute('readonly');")
        browser.execute_script("document.getElementsByClassName('picker__input')[1].removeAttribute('readonly');")

        txtSearch=browser.find_element(By.ID,"txtSearch")
        txtSearch.send_keys(artist)

        time.sleep(3)


        kaisaibi=array[1]

        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        kaisaiFrom=""
        kaisaidatesplit=kaisaibi.split("/")

        rainen=str(int(year)+1)
        
        print(kaisaibi)
        print(kaisaidatesplit[0])
        print(rainen)

        nen=kaisaidatesplit[0]
        if int(nen)==int(year) :
            kaisaiFrom=year
        elif int(nen)==int(rainen) :
             kaisaiFrom=rainen
        else :
            #今年でも来年でもない場合
            continue

        #月と日もセット
        kaisaiFrom=kaisaiFrom+"/"+kaisaidatesplit[1].rjust(2, '0')+"/"+kaisaidatesplit[2].split("(")[0].rjust(2, '0')



        print("check:"+kaisaiFrom)
        dateFrom=browser.find_element(By.ID,"dateFrom")
        #dateFrom.__delattr__("readonly")
        dateFrom.click()
        dateFrom.send_keys(kaisaiFrom)

        

        time.sleep(1)

#        browser.execute_script("document.getElementsById('dateTo')[0].removeAttribute('readonly');")
        if kaisaibi.find("～")>0 :
            kaisaiTo=""
            kaisaibiTo=kaisaibi.split("～")[1]
            kaisaidatesplitTo=kaisaibiTo.split("/")

            nen=kaisaidatesplitTo[0]
            if int(nen)==int(year) :
                kaisaiTo=year
            elif int(nen)==int(rainen) :
                kaisaiTo=rainen
            else :
                #今年でも来年でもない場合
                continue
           
            kaisaiTo=kaisaiFrom+"/"+kaisaidatesplitTo[1].rjust(2, '0')+"/"+kaisaidatesplitTo[2].split("(")[0].rjust(2, '0')
            dateTo=browser.find_element(By.ID,"dateTo")
            #dateTo.__delattr__("readonly")
            dateTo.click()
            dateTo.send_keys(kaisaiTo)
        else :
            dateTo=browser.find_element(By.ID,"dateTo")
            #dateTo.__delattr__("readonly")
            dateTo.click()
            dateTo.send_keys(kaisaiFrom)


        txtSearch.click()

        time.sleep(1)

        #cookies = browser.get_cookies() 
        #pickle.dump(cookies,open(cookies_file,'wb'))


        #一旦一番最初のみ
        break
    

#プログラムが終了すると勝手に閉じてしまう
time.sleep(1000000)

browser.quit()