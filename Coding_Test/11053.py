# 1127 9:35 ~ 10:35
# 1128 9:55 ~ 10:20
# ref - https://zidarn87.tistory.com/285

n = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n)]

# 조건이 두 개.
for i in range(n):
    for j in range(i):
        # print(i)
        # print(j)
        # print()

        # 1. 현재 원소(a[i])가 이전의 원소(a[j])보다 큰 경우에,
        # 2. 현재 위치의 dp[i]가 dp[j]보다 작은 경우
        # print(dp[i], dp[j])
        if a[i] > a[j] and dp[i] < dp[j]: 
            dp[i] = dp[j]
        # print()
    dp[i] += 1 # 먼저, dp[0]은 1로 초기화됨

# print(dp)
print(max(dp))