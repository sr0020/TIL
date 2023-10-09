# 1009 2:45 ~ 3:00, 
# 1010: 코드 구현 먼저 생각해보기

# 운전해야하는 거리의 최솟값
# https://maximum-curry30.tistory.com/349 (참고 - 삭제예정)

n, d = map(int, input().split())

# 지름길의 시작 위치, 도착 위치, 지름길의 길이
for _ in range(n):
    start, end, dis = map(int, input().split()) 


'''
1번 문제

10
+ 10
+ 10
+ 30 (지름길보다 기존의 길이 더 빠름)
+ 10
=> 70 
'''

'''
2번 문제

10
+ 40
+ 20
+ 10
=> 
'''