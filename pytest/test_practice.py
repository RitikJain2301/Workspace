import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

driver= None

def setup_module():
    global driver
    print("-------------setup method-------------")
    serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/chromedriver.exe")
    driver=webdriver.Chrome(service=serv)
    driver.get("https://www.google.com")
    
def teardown_module():
    print("-------------teardown method-------------")
    driver.quit()

def test_title():
    assert driver.title=='Google'

def test_title2():
    assert driver.title=='Google'

