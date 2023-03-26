x = 10
under_20 = x < 20

print(under_20)
print(not under_20)

# if문에 false 값 올 경우, 출력되지 않음
if False:
    print('false입니다.')

number = int(input('> '))

# 아래 조건문에서 number에 int형 0을 할당할 경우, print문 정상 작동
# str형으로 0을 할당할 경우, print문은 출력되지 않았음.
if number == 0:
    print('0입니다.')

import datetime
now = datetime.datetime.now()
print(now)