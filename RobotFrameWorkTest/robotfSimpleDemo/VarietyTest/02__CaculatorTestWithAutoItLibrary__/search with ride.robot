
Search Asset ID and Expect 400 Bad Request
    [Tags]
    Run Keyword And Expect Error    Request should have succeeded, but was "400 Bad Request".    Search Service    ${ASSET_PATH}search?program=+
    Run Keyword And Expect Error    Request should have succeeded, but was "400 Bad Request".    Search Service    ${ASSET_PATH}search?program=

Search Asset ID and Return Null with 400 Bad Request
    [Tags]    MEV-2167
    : FOR    ${INDEX}    IN RANGE    0    4
    \    Run Keyword And Continue On Failure    Run Keyword And Expect Error    Request should have succeeded, but was "400 Bad Request".    Search Service    @{SEARCH_RETURNNULL_200}[${INDEX}]
    \    ${RES_BODY}    Get Response Body
    \    Run Keyword And Continue On Failure    Should Be Equal    ${RES_BODY}    {"reason":"empty query text"}

Search Asset ID and Total Count Return Check
    [Documentation]    Need Data Preparation
    [Tags]    MEV-2168
    : FOR    ${INDEX}    IN RANGE    0    1
    \    Run Keyword And Continue On Failure    Search Service    ${ASSET_PATH}search?program=Girls
    \    Response Status Code Should Equal    200 OK
    \    ${RES_BODY}    Get Response Body
    \    ${GUID_COUNT}    Evaluate    str(${RES_BODY}).count('guid')
    \    Connect to MongoDB    ${_DB_SERVER}    8080
    \    ${allRes}    Retrieve Some Mongodb Records    ${_DB_NAME}    assets    {"program.name":"Girls"}
    \    Log    ${allRes}
    \    ${json_string}    Stringify Json    ${allRes}
    \    ${DB_COUNT}    Evaluate    str(${json_string}).count('guid')
    \    Should Be Equal As Integers    ${GUID_COUNT}    ${DB_COUNT}    Count Return Correct

Search Asset ID and Json Format and Value Check
    [Documentation]    Prepare data with program "urn":"hbo::program:op:grls".
    ...    "program":{"urn":"hbo::program:op:grls","code":"GRLS","name":"Girls"
    [Tags]    MEV-2168
    : FOR    ${INDEX}    IN RANGE    0    1
    \    Search Service    ${ASSET_PATH}search?program=Girls
    \    Response Status Code Should Equal    200 OK
    \    ${RES_BODY}    Get Response Body
    \    Should be Valid Json    ${RES_BODY}
    \    ${GUID_COUNT}    Evaluate    str(${RES_BODY}).count('guid')
    \    Should Contain X Times    ${RES_BODY}    "program":{"urn":"hbo::program:op:grls","code":"GRLS","name":"Girls"    ${GUID_COUNT}
