# 0806: 12:00 ~ 12:30
# 0808: 8:35 ~ 8:55, 9:20 ~ 10:40
# 0809: 10:25 ~ 11:55

# 카드가 갯수가 적고 가격이 비쌀수록 높은 등급의 카드가 있다 가정,
# 지불해야 하는 금액의 최댓값 구하기

"""
접근 방법
>> 작은 문제부터 생각해본다. 카드를 한개 사는법부터

dp[1] = p[1]
dp[2] = dp[1] + p[1] or dp[0] + p[2]
dp[3] = dp[2] + p[1] or dp[1] + p[2] or dp[0] + p[3]
dp[4] = dp[3] + p[1] or dp[2] + p[2] or dp[1] + p[3] or dp[0] + p[4]

현재 카드를 지불하는 최대 금액(p)과 
이전의 카드를 지불한(i - j) 최대 금액 + j개가 들어있는 카드팩 가격(p)을 비교
"""

# input
n = int(input())
dp = [0] * (n+1) # dp 테이블
p = [0] + list(map(int, input().split())) # pi: 가격, i: 카드 갯수
# print(p)

for i in range(1, n+1):
    for j in range(1, i+1):
        # print(i, i-j, ' ', dp[i], p[j], dp[i-j], p[j] + dp[i-j])
        dp[i] = max(dp[i], p[j] + dp[i-j])
    # print()

# 금액의 최댓값 출력
print(dp[n])