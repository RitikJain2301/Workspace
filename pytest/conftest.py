import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver=None

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption('--browserr')

@pytest.fixture(scope="session", autouse=True)
def tc_setup(browser):
    global driver
    if  browser=="chrome":
        serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/chromedriver.exe")
        driver=webdriver.Chrome(service=serv)
    elif browser=="edge":
        serv=Service("C:/Users/Administrator/AppData/Local/Programs/Browsers/msedgedriver.exe")
        driver=webdriver.Edge(service=serv)  
    return driver

def pytest_addoption(parser):   
    parser.addoption('--browserr')

