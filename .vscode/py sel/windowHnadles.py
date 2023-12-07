import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/msedgedriver.exe")
driver=webdriver.Edge(service=serv)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='View All']").click()

print(driver.window_handles())