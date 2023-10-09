# 0926 1:41 ~ 1:53, 0928 5:30 ~ 6:00, 0930 3:30 ~ 4:00, 
# 1009 2:30 ~ 2:45
from collections import deque

# BFS (인접한 노드 먼저 탐색)
# 참고로 DFS (재귀, 다음 분기로 넘어가기 전 해당 분기를 완벽하게 탐색해야 함)

# BFS. 
def BFS(v):
    q = deque([v])
    visited[v] = 1

    while q:
        t = q.popleft()
        # print(q)

        for i in g[t]:
            if not visited[i]:
                visited[i] = visited[t] + 1
                q.append(i)


# n: 유저의 수, m: 친구 관계
n, m = map(int, input().split())
g = [[] for _ in range(n+1)] # 연결된 간선 저장하는 배열

for _ in range(m):
    a, b = map(int, input().split()) # 친구 관계
    g[a].append(b)
    g[b].append(a)

# 케빈 베이컨의 수가 가장 작은 사람 - BFS를 통해 케빈 베이컨과 가장 가까운 사람
# ==> BFS 횟수가 가장 적은 사람
# + 횟수가 적은 사람이 여러 명일 경우, 가장 작은 인덱스(사람) 출력
result = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    BFS(i)
    result.append(sum(visited)) # sum - 방문한 횟수 더함

# print(g)
print(result.index(min(result))+1) # max 아니고 min