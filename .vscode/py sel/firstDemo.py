# from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/chromedriver.exe")
# driver=webdriver.Chrome(service=serv)
# # driver=Chrome.webdriver
# driver.get("https://www.google.com")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
serv=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=serv)
driver.get("https://www.google.com")
# driver = webdriver.Chrome()
# time.sleep(3)
driver.find_element(By.XPATH,"")