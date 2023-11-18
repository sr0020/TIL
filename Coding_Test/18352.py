# 다익스트라 (BFS 기반)
# 1111 2:30 ~ 2:40
# 1118 4:10 ~ 5:00

# X로부터 출발하여 도달할 수 있는 도시 중에서, 
# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력

# 1. BFS, DFS 사용하는 상황 구분하고..
# 2. 이 상황에서 BFS가 왜 맞는 건지 문제와 연관지어서 이해

from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1) # 거리 저장
visited = [0] * (n+1) # 방문 배열 저장

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b) # a번째 인덱스에 b를 넣음으로써, a와 b노드가 연결되었음을 표시

def bfs(s):
    answer = []
    q = deque([s]) # 최종적으로 처리해서 answer에 담을 배열
    visited[s] = True
    distance[s] = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i) # i번째 노드 방문처리 후 q에 담기
                distance[i] = distance[now] + 1 
                if distance[i] == k:
                    answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x) # x번째 노드에서 탐색 시작한다는 의미