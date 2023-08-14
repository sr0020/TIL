# 순차탐색
def func(n, name, arr):
    # print(type(n), type(name), type(arr))

    for i in range(0, int(n)):
        if name == arr[i]:
            return i + 1 # index 리턴

# 생성할 원소 갯수 및 찾을 이름
n, name = input().split()
# print(n, name)

# 생성할 원소 갯수만큼 문자열 받기
arr = list(input().split())
# print(arr)

result = func(n, name, arr)
print(result)