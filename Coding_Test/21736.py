# 1119 2:40 ~ 3:20

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y): # 2차원 배열에서 DFS 수행
    global cnt # cnt 변수 전역으로 선언
    visited[x][y] = True
    if info[x][y] == 'P':
        cnt += 1

    for i in range(4):
        nx = x + dx[i] # nx => 다음에 방문할 x 좌표
        ny = y + dy[i]
        # nx, ny가 방문된 경우, 바로 cnt += 1 처리됨

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if info[nx][ny] != 'X':
                dfs(nx, ny)

    # nx, ny 방향대로 돌고, P가 나오는 경우 cnt += 1

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
info = list(input() for _ in range(n))
visited = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if info[i][j] == 'I':
            dfs(i, j)

if cnt == 0:
    print('TT')
else:
    print(cnt)