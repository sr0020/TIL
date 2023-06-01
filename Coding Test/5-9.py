from collections import deque

def bfs(graph, s, visited): 
    q = deque([s])
    visited[s] = True # 

    while q: # 
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True #

graph = [
    [], # 노드 0과 연결된 인접 노드
    [2, 3, 8], # 노드 1과 연결된 인접 노드
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

result = [False] * 9
bfs(graph, 1, result)