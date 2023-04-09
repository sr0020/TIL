# 1
# TypeError: f() missing 2 required keyword-only arguments: 'valueA' and 'valueB'
# 1~5 전부 *values로 받아버려서 valueA, valueB에 값이 할당되지 않은 상태
# def f(*values, valueA, valueB):
#     for value in values:
#         print(value) # 1 2 3 4 5

#     print(valueA) 
#     print(valueB) 

# f(1, 2, 3, 4, 5)

# # 2
# def f(*values, valueA=10, valueB=20):
#     for value in values:
#         print(value) # 1 2 3 4 5

#     print(valueA) # 10
#     print(valueB) # 20

# f(1, 2, 3, 4, 5)

# 4
# 키워드 매개변수가 일반 매개변수보다 뒤에 있을 경우 오류 발생하지 않음
def f(valueA=10, valueB=20, *values):

    print(valueA) # 1로 재정의됨
    print(valueB) # 2로 재정의됨

    for value in values:
        print(value) # 3 4 5

f(1, 2, 3, 4, 5)