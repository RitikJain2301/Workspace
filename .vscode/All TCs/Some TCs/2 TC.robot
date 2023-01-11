*** Settings ***
Resource    ../TCs.robot
Library    SeleniumLibrary

*** Test Cases ***
Test 2a TC        
    Open Browser    https://www.youtube.com/   Chrome
    ${HTML}    Get Source
    log  ${HTML}

Test 2b TC
    Log    this is my 2b TC
    