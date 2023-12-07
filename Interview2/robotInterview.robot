*** Settings ***
Library     SeleniumLibrary
Library    pyth.py

*** Variables ***
${URL}=    google.com

*** Keywords ***

*** Test Cases ***
TC_001
    ${po}     pyth.This For
    Log To Console    ${po}
    
    
