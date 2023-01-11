*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
open Test    
    Open Browser    https://www.google.co.in/    Chrome
    Set Selenium Speed    3
    Input Text    css=.gLFyf    test
    ${speedG}=    Get Selenium Speed
    Log    ${speedG}
    Capture Page Screenshot
    Select Checkbox    m
    Click Element    ds