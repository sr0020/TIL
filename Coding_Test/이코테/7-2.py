# 이진 탐색
# 원하는 숫자가 몇 번째에 있는지 찾는(숫자의 인덱스를 찾는) 코드

def func(target, arr, start, end):

    mid = (start + end) // 2 

    # print('mid = ', mid)
    # print(start, end)
    # print(arr[mid], target)

    # 1. 찾으려는 숫자(target)와 mid값이 일치할 경우 return
    if arr[mid] == target:
        return mid # mid 값이 한 개가 될 때까지 분할하는 방식
    
    # 2. 찾으려는 숫자의 index보다 mid값이 작은 경우
    elif arr[mid] < target:
        # print("2. 찾으려는 숫자의 index보다 mid값이 작은 경우")
        # print(mid, end)
        return func(target, arr, mid+1, end) # mid 값 다음부터 end까지

    # 3. 찾으려는 숫자의 index보다 mid값이 큰 경우
    elif arr[mid] > target:
        # print('3. 찾으려는 숫자의 index보다 mid값이 큰 경우')
        # print(start, mid)
        return func(target, arr, start, mid-1) # start부터 mid값 바로 전까지

# 총 데이터의 갯수 및 찾으려는 문자열 입력
n, target = list(map(int, input().split())) # map(int, ...)은 리스트의 모든 요소를 int 함수를 통해 정수로 변환
# print(type(n))

# 문자열 입력
arr = list(map(int, input().split())) 

start, end = 0, len(arr)-1

result = func(target, arr, start, end)
print('result = ', result + 1)