# # 1. random 모듈
# from random import random, randrange, choice, uniform, shuffle, sample
# print("# random 모듈")

# # random(): 0.0 <= x < 1.0 사이의 float를 리턴합니다.
# print("- random():", random())

# # uniform(min, max): 지정한 범위 사이의 float를 리턴합니다.
# print("- random(10, 20):", uniform(10, 20))

# # randrange(): 지정한 범위의 int를 리턴합니다.
# # - randrange(max): 0부터 max 사이의 값을 리턴합니다.
# # - randrange(min, max): min부터 max 사이의 값을 리턴합니다.
# print("- randrange(10):", randrange(10))

# # choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
# print("- choice([1, 2, 3, 4, 5]):", choice([1, 2, 3, 4, 5]))

# # shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
# print("- shuffle([1, 2, 3, 4, 5]):", shuffle([1, 2, 3, 4, 5]))

# # sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
# print("- sample([1, 2, 3, 4, 5]):", sample([1, 2, 3, 4, 5], k=2))

# # 2. sys 모듈
# import sys

# # 명령 매개변수
# print("---")
# print(sys.argv)
# print("---")

# print(sys.getwindowsversion())
# print("---")
# print(sys.copyright)
# print("---")
# print(sys.version)
# print("---")

# sys.exit()

# # 3. os 모듈
# import os

# print("---")
# print(os.name)
# print(os.getcwd())
# print(os.listdir())

# os.mkdir("hello")
# os.rmdir("hello")

# with open("org.txt", "w") as f:
#     f.write("hello")
# os.rename("org.txt", "new.txt")

# os.remove("new.txt")
# os.system("dir")

# # 4. urllib 모듈
# from urllib import request

# target = request.urlopen("https://www.google.com/")
# output = target.read()

# print(output)

# # 5. itemgetter
# from operator import itemgetter

# books = [{
#     "제목": "혼자 공부하는 파이썬",
#     "가격": 18000
# }, {
#     "제목": "혼자 공부하는 머신러닝 + 딥러닝",
#     "가격": 26000
# }, {
#     "제목": "혼자 공부하는 자바스크립트",
#     "가격": 24000
# }]

# def 가격추출함수(book):
#     return book["가격"] # book["가격"] 변수는 딕셔너리의 값을 의미함.

# print("# 가장 저렴한 책")
# print(min(books, key=itemgetter("가격")))
# print()

# print("# 가장 비싼 책")
# print(max(books, key=itemgetter("가격")))

# 6. datetime
import datetime
now = datetime.datetime.now()

after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)

print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))