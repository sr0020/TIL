n, m = map(int, input().split())
x, y, dir = map(int, input().split())
arr = []
cnt = 1

for i in range(n):
    arr.append(list(map(int, input().split())))

dist = [0, 1, 2, 3] # 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while(1):
    arr[x][y] = 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 진행한 방향에 육지 존재할 경우 +1
    if arr[nx][ny] == 0:
        x = nx
        y = ny
        arr[nx][ny] = 1
        cnt += 1

    # 방향 탐색
    if dir < 4:
        dir += 1
        print('dir = ', dir)
    else:
        dir = 0

    # N행까지 진행 완료된 경우 프로그램 종료
    count_n = 0
    for i in arr:
        if 0 not in i:
            count_n += 1
    if count_n == n:
        break

print(cnt)