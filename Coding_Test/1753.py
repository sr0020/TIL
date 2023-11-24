# 1120 9:35 ~ 10:25
# 1120 9:15 ~ 9:35

# 다익스트라 기본

# 첫째 줄부터 V개의 줄에 걸쳐, 
# i번째 줄에 "i번 정점으로의 최단 경로의 경로값"을 출력
# i가 end 지점이 되는 최단 경로의 경로값

# heap => 가장 낮은(혹은 높은) 우선순위를 가지는 노드가 항상 루트에 오게

# 만들어져야 하는 배열: graph, distance, heapq 구조 가지는 배열 q
# 만들어져야 하는 변수: INF (최단 경로 값 저장)

# 1. 기본 함수, 2. 정답 도출 및 활용 부분 

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# print(INF)

def dijkstra(start):
    # 초기화
    q = [] # 거리, 정점 쌍 저장됨
    heapq.heappush(q, (0, start)) # q에 (0, start)를 push
    distance[start] = 0

    # dist: 현재까지의 최단 거리, now: 현재의 정점
    while q:
        dist, now = heapq.heappop(q)

        # 최단 거리 갱신된 경우 continue
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 인접 노드 확인하며 최단 거리 갱신
        for i in graph[now]:
            # print(i)
            cost = dist + i[1] # 가중치 (i[1] 역시 가중치(= 비용, 간선))
            if cost < distance[i[0]]:
                distance[i[0]] = cost

                # 최단 거리, 정점을 힙에 삽입
                heapq.heappush(q, (cost, i[0]))

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1) # 최단 거리 테이블. V개 저장

for _ in range(E):
    u, v, w = map(int, input().split()) # start, end, weight
    graph[u].append((v, w)) # 노드에 end, weight를 tuple 형태로 추가

dijkstra(K)  

# 정답 부분
# i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])