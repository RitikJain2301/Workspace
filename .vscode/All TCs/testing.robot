*** Settings ***
Library    SeleniumLibrary
# Library    Collections

*** Variables ***
@{maxa}=    create list    tyh    mhgvmn

*** Test Cases ***
TC_001
    FOR    ${counter}    IN RANGE    1    10
        Log To Console   ${counter}
    END