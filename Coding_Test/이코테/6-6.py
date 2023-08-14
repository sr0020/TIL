# 계수 정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
result = []

seq = [x for x in range(10)]
cnt = [0 for _ in range(10)]
# print(cnt)

for i in range(len(arr)):
    if arr[i] in seq:
        # arr[i]의 값과 seq의 i값이 일치할 경우
        cnt[arr[i]] += 1 # 

# print(cnt)

for i in range(len(cnt)):
    # 0 인덱스의 값(cnt[0])은 2. 0을 2번 출력
    for j in range(cnt[i]):
        result.append(i)

print(result)