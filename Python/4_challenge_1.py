# 사용된 숫자의 종류 구하는 프로그램

arr = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
result = {}

for i in arr:
    if i in result: # result안에 요소가 없는 경우 1씩 더함.
        result[i] += 1
    else:
        result[i] = 1

print("{}에서\n사용된 숫자의 종류는 {}개입니다.".format(arr, result))
print("참고: {}".format(result))