# 5:40 ~ 6:50 (0708) - 시간초과
# 3:55 ~ 4:02 (0710)

"""
서류 순위로 지원자 정렬 후, 
정렬했을 때 앞 지원자(서류순위가 높은 지원자)보다 
면접순위 높은 지원자 선발하는 문제
"""

import sys

t = int(input())
result = 0
temp = []

for i in range(t):
    n = int(input())
    temp = []

    for _ in range(n):
        docu, inter = map(int, sys.stdin.readline().split()) # input() => sys.stdin.readline()
        temp.append([docu, inter])

    # 서류성적 기준으로 정렬
    temp.sort(reverse=False)

    # 면접 성적 기준으로 정렬
    count = 1 # 서류 성적은 이미 정렬되었고, 1번 지원자는 무조건 합격하기에
    max_inter = temp[0][1]

    for i in range(1, n):
        if max_inter > temp[i][1]: # 1번 지원자보다 현재 지원자가 순위가 높은 경우
            count += 1 # 선발
            max_inter = temp[i][1]
            # print('i = ', i, 
            #       ', max (면접 순위 현재 max 순위 지원자보다 높은 지원자 순위) = ',
            #     max_inter)

    print(count)