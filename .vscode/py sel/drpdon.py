import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

##dropdown
driver=webdriver.Chrome("C:/Users/Administrator/AppData/Local/Programs/Browsers/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
# drp=Select(B)
# drp.select_by_value("")

# ##handle alert
# alrt=driver.switch_to.alert
# alrt.accept()

# ##frames
# driver.switch_to.frame

##action chains mouse actions
ac=ActionChains(driver=driver)
ac.double_click(driver.find_element(By.XPATH,"//button[text()='Copy Text']")).perform()
time.sleep(3)

##actions chains keyboard actions
ac.key_down(Keys.CTRL)
##scroll
driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element(By.XPATH,"//button[text()='Copy Text']"))
time.sleep(3)

#scroll by pixels
driver.execute_script("window.scrollBy(0,300)","")

###scroll into view by element\
driver.execute_script("arguments[0].scollIntoView();",)