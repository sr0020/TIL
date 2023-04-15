# 좀 더 알아보기

# #
# def test():
#     print("함수가 호출되었습니다.")
#     yield "test"

# print("A 지점 통과")
# test()

# print("B 지점 통과")
# test()
# print(test())

# # 
# def test():
#     print("A 지점 통과")
#     yield 1
#     print("B 지점 통과")

# output = test()

# print("D 지점 통과")
# a = next(output)
# print(a)

# print("E 지점 통과")
# b = next(output) # next() 함수 호출 이후 yield 키워드 없는 경우 StopIteration
# print(b)

# print("F 지점 통과")
# c = next(output)
# print(c)

# next(output)

# key 키워드 매개변수
books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]

def 가격추출함수(book):
    return book["가격"] # book["가격"] 변수는 딕셔너리의 값을 의미함.

print("# 가장 저렴한 책")
print(min(books, key=가격추출함수)) # "가격" 값을 비교
print(min(books, key=lambda book: book["가격"]))
print()

print("# 가장 비싼 책")
print(max(books, key=가격추출함수)) # "가격" 값을 비교
print(max(books, key=lambda book: book["가격"]))

print("# 가격 오름차순 정렬")
books.sort(key=lambda book: book["가격"])
for book in books:
    print(book)

print(type(books))

# 기본 자료형 복사
def ex(b):
    b = 20

    return b

a = 10

print(a)
ex(a) 
print(ex(a)) # a값을 20으로 출력하고 싶다면, ex함수를 출력해야 함(return받은 b값 출력. 리턴 값 없을 경우 None 출력)
print(a) # 전역 스코프에 존재하는 a값은 변경되지 않음.

# global 키워드
aa = 10

def func():
    global aa # 전역변수는 함수 내부에서 global 선언을 해줘야 사용가능
              # 해당 키워드 없을 시 UnboundLocalError: local variable 'aa' referenced before assignment 발생
    print('aa =', aa)
    aa = 20

func()