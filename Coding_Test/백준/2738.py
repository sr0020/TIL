n, m = map(int, input().split())

for _ in range(n):
    row_1 = list(map(int, input().split()))

for _ in range(n):
    row_2 = list(map(int, input().split()))

for i in range(n):
    result = []
    for j in range(m):
        element = 0
        element += row_1[i][j] + row_2[i][j]
        result.append(element)

    print(result)