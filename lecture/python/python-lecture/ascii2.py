ascii = input('입력 : ')
ascii = int(ascii)

min = 1
max = 127
cha = 0
while min != max:
    avg = (min + max) / 2
    print("{}차 {} ~ {} 평균값 {}".format(cha, min, max, avg))
    if ascii > avg:
        min = avg + 1
    else:
        max = avg
    
    if ascii > avg:
        min = avg + 1
        print("{} > {} -> 참".format(ascii, avg))
    else:
        max = avg
        print("{} > {} -> 거짓".format(ascii, avg))

print('아스키 값은 : ' + str(int(min)) + '입니다.')
# ascii > 65 참 65~127, 거짓 1~64

