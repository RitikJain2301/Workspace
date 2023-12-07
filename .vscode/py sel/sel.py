import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.implicitly_wait(3)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"seventh-largest country").click()
time.sleep(3)
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("ritik jain")
driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
alertWin=driver.switch_to.alert
time.sleep(3)
alertWin.accept()
driver.save_screenshot("C:/Users/Administrator/AppData/Local/Programs/Workspace/ss2.png")
drp=Select(driver.find_element(By.ID,"speed"))
drp.select_by_visible_text("Medium")
ac=ActionChains(driver)

drag=driver.find_element(By.ID,"draggable")
drop=driver.find_element(By.ID,"droppable")
ac.drag_and_drop(drag,drop).perform()
time.sleep(3)
print(driver.title)