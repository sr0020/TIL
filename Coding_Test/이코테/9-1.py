import sys
input = sys.stdin.readline
INF = int(1e9)

# 초기화
# 노드의 갯수, 간선의 갯수를 입력받기
v, e = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(v+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [0] * (v+1)

# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v+1)

# input
# 모든 간선 정보를 입력받기
for _ in range(e):
    a, b, c = map(int, input().split()) # a, b가 간선이고 c가 cost(가중치)
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def small_dis():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드 (인덱스)

    for i in range(1, v+1):
        if distance[i] < min_value or not visited[i]:
            min_value = distance[i]
            index = i

    return index

# 다익스트라 함수
def dik(start):

    distance[start] = 0 # 시작 노드에 대해서 초기화
    visited[start] = 1
    for j in graph[start]: # graph[start] - 노드에 연결된 간선 및 cost를 담은 배열
        distance[j[0]] = j[1] # distance 배열의 j[0]번 노드에 j[1] cost 대입

    for i in range(v-1): # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복

        # 노드의 cost가 짧은 순으로 방문처리
        now = small_dis() # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        visited[now] = 1

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 수행
# 함수 진행과정은 이해했음. 문제는 input으로 들어온 간선, cost가 어떻게 처리되는지를 모르게씅ㅁ
dik(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, v+1):
    
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")

    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

