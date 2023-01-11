*** Settings ***
Library    SeleniumLibrary
Library    open.py
*** Keywords ***
setting up test
    Input Text    name:search_query    Nice
setting up teardown test
    Press Keys   name:search_query    CTRL+'R'
set suite setu
    Open Browser    https://www.youtube.com/   Chrome
    Maximize Browser Window
    Set Selenium Speed    2
    Sleep    3
set suite tear
    Close All Browsers

*** Test Cases ***
TCtest
    ${test}=     Check Rob
    Log To Console    ${test}
    