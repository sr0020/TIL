# 반복문 사용
iter = []

for i in range(0, 20, 2):
    iter.append(i*i)

print("반복문 활용: ", iter)

# 리스트 내포
array = []

array = [i * i for i in range(0, 20, 2)]

print("리스트 컴프리핸션: ", array)

# 좀 더 알아보기
# 
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(number, number))

# 바로 위 코드와 동일한 출력
number = int(input("정수 입력> "))

if number % 2 == 0:
    print(("입력한 문자열은 {}입니다.\n"
          "{}는(은) 짝수입니다.")
        .format(number, number))
else:
    print(("입력한 문자열은 {}입니다.\n"
          "{}는(은) 짝수입니다.")
        .format(number, number))
    
# 이터레이터
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print(r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))