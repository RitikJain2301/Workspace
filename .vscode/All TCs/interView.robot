*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${URL}     https://testautomationpractice.blogspot.com/
${Chrome}    Chrome

*** Test Cases ***
TC001
    # Set Selenium Speed    1s
    Open Browser     ${URL}    ${Chrome}
    Maximize Browser Window
    Input Text    id=Wikipedia1_wikipedia-search-input    this is text
    Click Element    xpath=//button[text()="Click Me"]
    Handle Alert    Accept
    Select From List By Label    id=speed    Medium
    Sleep    2s
    # Select Radio Button    name=ItemAnchor7    Male
    Capture Page Screenshot
    Drag And Drop    id=draggable    id=droppable