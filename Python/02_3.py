import math

# 02-3
string = "안녕하세요" # * "안녕하세요" # TypeError: can't multiply sequence by non-int of type 'str'
print('String: ', string)

t = input('> ')
print(type(t)) # 'True' 입력할 경우 bool형이 아닌 str형으로 출력됨

print(int(3.141952)) # 3
# print(int('3.141952')) # ValueError: invalid literal for int() with base 10: '3.141592'

# # 4
# str_input = input('숫자 입력 > ')
# num_input = int(str_input)

# print()
# print(num_input, "inch")
# print((num_input * 2.54), 'cm')

# 5
str_input = input("원의 반지름 입력 > ")
num_input = int(str_input)

print()
print("반지름: ", num_input)
print("둘레: ", 2 * 3.14 * num_input)
print("넓이: ", 3.14 * num_input * num_input)

# 6
# 1. 문자열 a, b 순서대로 출력, 2. swap한 a, b 출력
def swap(a, b):
    temp = a
    a = b
    b = temp

    return a, b

a = input("문자열 입력 > ")
b = input("문자열 입력 > ")

print(a, b)
a, b = swap(a, b) 

print(a, b)