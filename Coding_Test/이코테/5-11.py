# 미로 탈출
from collections import deque

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

visited = []

def bfs(x, y):
    queue = deque([x][y])
    visited[x][y] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False

print(bfs(0, 0))