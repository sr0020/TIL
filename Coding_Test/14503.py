# 1125 3:53 ~ 6:00

# 로봇 청소기가 작동을 시작한 후 멈출 때까지 청소하는 칸의 개수

import sys
input = sys.stdin.readline

# 청소기는 d가 0일 경우 동쪽을 바라보고, 아래 dx dy는 이 방향 기준으로 결정했음
# 북 (-1, 0), 동 (0, 1), 남 (1, 0), 서 (0, -1)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 후진 
def get_back(x, y, d):
    if d == 0 or d == 1:
        nx = x + dx[d+2] # d+2 뜻: 북(0) => 남(2)으로 변경
        ny = y + dy[d+2] # 동(1) => 서(3)으로 변경
    if d == 2 or d == 3:
        nx = x + dx[d-2]
        ny = y + dy[d-2]
    return nx, ny

# input
n, m = map(int, input().split())
graph = []

# d는 동, 서, 남, 북 중 하나이고, 앞의 방향은 각각 0, 1, 2, 3임
# + d와 dx, dy는 다른 변수임.
r, c, d = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))

v = [[0] * m for _ in range(n)]
v[r][c] = 1
count = 1

# 구현
while True:
    unavail = 0

    for _ in range(4):
        nx = r + dx[(3+d)%4]
        ny = c + dy[(3+d)%4]

        if 0 <= nx < n and 0 <= ny < m and \
            graph[nx][ny] == 0 and v[nx][ny] == 0:
            
            d = (3+d) % 4 # (반시계 방향) 0, 3, 2, 1 순서 (d가 0일 경우)
            v[nx][ny] = 1
            r = nx
            c = ny
            count += 1
            unavail = 1 # 청소 가능한 지역이 존재하기에, 1로 변경
            break

        else: # 4가지 방향 다 청소 가능한지 확인 
            d = (3+d)%4

    # 청소가능한 지역이 동서남북, 후진 모두에 없는 경우
    if unavail == 0:
        a, b = get_back(r, c, d)
        if graph[a][b] == 1:
            break
        else:
            r, c = a, b

print(count)