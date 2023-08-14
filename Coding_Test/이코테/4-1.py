n = int(input())

arr = input().split()
# print(type(arr))

x, y = 1, 1

dist = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1] # x가 행 (세로 방향으로 직진)
dy = [-1, 1, 0, 0] # y가 열 (가로 방향으로 직진)

for i in arr:
    # print(i)
    for j in range(len(dist)):
        if dist[j] == i:
            nx = x + dx[j]
            ny = y + dy[j]

    if ny > n or ny < 1 or nx > n or nx < 1:
        continue

    x, y = nx, ny

print(x, y)