import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

##dropdown
serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/msedgedriver.exe")
driver=webdriver.Edge(service=serv)
driver=webdriver.Edge("C:/Users/Administrator/AppData/Local/Programs/Browsers/msedgedriver.exe")
# serv=Service(ChromeDriverManager().install())
# driver=webdriver.Chrome(service=serv)


driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(10)
driver.maximize_window
time.sleep(5)
driver.find_element(By.XPATH,"//*[@class='icon_calendar']").click()
year=Select(driver.find_element(By.XPATH,"//*[@class='ui-datepicker-year']"))
year.select_by_value('2017')

while   driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text != 'January':
    driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
