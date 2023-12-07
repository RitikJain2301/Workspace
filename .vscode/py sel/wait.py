from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.service import Service

serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://www.google.com/")

##implicit wait
driver.implicitly_wait(3)

## explicit wait
wait=WebDriverWait(driver,10,ignored_exceptions=Exception )
wait.until(EC.presence_of_element_located((By.NAME,"q")))