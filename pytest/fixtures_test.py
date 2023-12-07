import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(request):
    
    serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/chromedriver.exe")
    web_driver=webdriver.Chrome(service=serv)
    web_driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(5)
    request.cls.driver=web_driver
    yield 
    web_driver.fullscreen_window()

@pytest.mark.usefixtures("setup")
def test1(web_driver):
    ac=ActionChains(driver=web_driver)
    ac.double_click(web_driver.find_element(By.XPATH,"//button[text()='Copy Text']")).perform()
    time.sleep(6)