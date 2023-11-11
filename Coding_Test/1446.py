# 현재상태 - DFS, BFS, 최단경로 등 중급? 알고리즘 원리 이해 시작해야 하는 상태

# 1009 2:45 ~ 3:00, 
# 1010: 10:10 ~ 10:40 (코드 구현방법 고민)
# 1026: 11:00 ~ 12:00

# 운전해야하는 거리의 최솟값
# 접근은 쉬운데 구현이 어려운 문제 (생각을 코드화시키는 게 어려웠음)

n, d = map(int, input().split())

# 지름길의 시작 위치, 도착 위치, 지름길의 길이 담은 배열
g = [list(map(int, input().split())) for _ in range(n)] 

# d 저장하는 배열
dis = [i for i in range(d+1)]

for i in range(d+1):
    dis[i] = min(dis[i], dis[i - 1] + 1)

    for s, e, short in g:
        if i == s and e <= d: # s: 각 시작점
            dis[e] = min(dis[e], dis[i] + short) # 원 경로, 지름길 중 짧은 길 선택
        
print(dis[-1])


'''
1번 문제

10
+ 10
+ 50
=> 70 
'''

'''
2번 문제

10
+ 40
+ 20
+ 10
=> 80
'''