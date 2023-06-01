m, n = map(int, input().split())
arr = []
result = []

for i in range(m):
    arr.append(list(map(int, input().split())))
    min_num = min(arr[i])
    result.append(min_num)
    # print(min_num)

print(max(result))