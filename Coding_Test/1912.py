# 1912
# 9:45 ~ 10:20

n = int(input())
dp = list(map(int, input().split()))
# print(n)

for i in range(1, len(dp)): # 범위
    # print(i, dp[i], dp[i] + dp[i-1])
    dp[i] = max(dp[i], dp[i] + dp[i-1])
    # print(i, dp[i])
    # print()

print(max(dp))