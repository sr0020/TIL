def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]: # 방문되지 않은 경우
            dfs(graph, i, visited) # 인접 노드 탐색
            
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
dfs(graph, 1, result)