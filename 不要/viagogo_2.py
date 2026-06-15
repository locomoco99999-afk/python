from selenium import webdriver
from selenium.webdriver.chrome import service as chrome_service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

ID="fmbt03@yahoo.co.jp"
#PASSWORD=""

#chrome://version

cs = chrome_service.Service(executable_path = r'C:/phython/chrome/chromedriver.exe')

options = Options()

profile_path="C:/Users/locom/AppData/Local/Google/Chrome/User Data/Profile/"
binary_location = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe' 
options.add_argument('--user-data-dir=' + profile_path)
options.add_argument('--profile-directory=Default')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

webd = webdriver.Chrome(service = cs,options=options)
webd.get('https://my.viagogo.jp/orders')


time.sleep(2)


#loginTX = webd.find_element(By.ID,'Login_UserName')
#loginTX.send_keys(ID)

#passwordTX=webd.find_element(By.ID,"Login_Password")
#passwordTX.send_keys(PASSWORD)

#loginBT=webd.find_element(By.ID,"sbmt")
#loginBT.click()


#プログラムが終了すると勝手に閉じてしまう
time.sleep(1000000)