*** Settings ***
Resource    ../TCs.robot
Library    SeleniumLibrary
*** Test Cases ***
Test 1a TC        
    Input Text    name:search_query    Picture
Test 1b TC
    Input Text    name:search_query    Nice picture dear
    
*** Keywords ***
