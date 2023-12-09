# 9:20 ~ 10:35
# https://hongcoding.tistory.com/157

# 없애야 하는 전깃줄의 최소 갯수
# 최장 증가 부분 수열 - https://4legs-study.tistory.com/106
n = int(input())
temp = []
dp = [1 for _ in range(n)]

# A 전봇대에서 그리디 방식으로 전깃줄 없애기
for _ in range(n):
    a, b = map(int, input().split())

    temp.append([a, b])

temp.sort()
# print(temp)

# print()
for i in range(1, n):
    # print('i = ', temp[i])

    for j in range(0, i):
    #     print('j = ', temp[j])
    # print()

        if temp[i][1] > temp[j][1]:
            # print('*'*10)
            # print(i, j)
            # print('temp[i][1] = ', temp[i][1], \
            #       'temp[j][1] = ', temp[j][1])
            # print(dp[i], dp[j])
            dp[i] = max(dp[i], dp[j]+1) 

    # print(dp)
    # print()

# dp[i]는 존재해야 하는 전깃줄의 갯수. 
# 남아있는 전깃줄의 갯수 - 최대 증가 부분 수열
print(n - max(dp))

# dp의 각 i번째 마다 조건이 해당할 경우 dp의 인덱스 요소 값이 바뀜