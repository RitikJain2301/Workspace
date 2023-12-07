*** Settings ***
Library    SeleniumLibrary
# Library    Collections

*** Variables ***
@{maxa}    create list    tyh    mhgvmn

*** Test Cases ***
TC_001
    FOR    ${counter}    IN     @{maxa}
        Log To Console   ${counter}
    END

TC_002
    Log To Console     ${maxa}[1]
    