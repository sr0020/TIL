# (0823) 3:30 ~ 4:30

t = int(input())
dp = [1] * 101 # dp 배열의 크기가 101이 아닌 100인 경우 indexerror(런타임 에러)
               # dp에 100이 n으로 들어오는 경우, 아래 for문의 n+1에서 에러

# 점화식: p(n) = p(n-2) + p(n-3)

# # dp 테이블 예시
# for i in range(3, 100):
#     dp[i] = dp[i-2] + dp[i-3]

# n에 대하여 dp(n) 구하기
for _ in range(t):
    n = int(input())

    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    
    print(dp[n-1])
