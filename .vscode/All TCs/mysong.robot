*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TC_001
    Open Browser    https://www.youtube.com/   Chrome
    Maximize Browser Window
    Input Text    name:search_query    Khabarein Rap Junkie
    Click Element    css=#search-icon-legacy
    
    WHILE    True
        Sleep    2s
        Play my song
    END
    

*** Keywords ***
Play my song
    Click Element    xpath=//a[contains(@aria-label,'Khabarein ')]
    Sleep    15s
    Press Keys    css=#search-icon-legacy    CTRL+'R'