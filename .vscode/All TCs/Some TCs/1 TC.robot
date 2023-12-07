*** Settings ***
# Resource    ../TCs.robot
Resource     2 TC.robot
Library    SeleniumLibrary
*** Test Cases ***
Test 1a TC        
    Input Text    name:search_query    Picture
Test 1b TC
    Input Text    name:search_query    Nice picture dear

Test
    This is a import keyword
    # Open Browser    https:\\www.google.com     Chrome
    
*** Keywords ***
 