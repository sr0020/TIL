import datetime

s = input('> ')
n = datetime.datetime.now()
temp = n.hour # callable = 호출 가능한 클래스, 인스턴스, 함수, 메서드 등 객체
# print(temp)

if s == '안녕':
    print('안녕하세요')
elif s == '안녕하세요':
    print('안녕하세요')
elif s == '지금 몇 시야':
    print('지금은 '+ str(temp) + '시 입니다.')
else:
    print(s)