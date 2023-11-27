# 1126 3:50 ~ 5:15
# 1127 12:50 ~ 1:20

tmp = []

n = int(input()) # n + 1일째 날 퇴사 예정
for _ in range(1, n+1):
    t, p = map(int, input().split()) # time, pay
    tmp.append([t, p])

# print(tmp)

dp = [0 for _ in range(n+1)]
# print(dp)

# 결과 구하기
# 거꾸로 for문
for i in range(n-1, -1, -1):
    # print(i)
    if tmp[i][0] + i <= n:

        # dp[i+tmp[i][0]]
        #  현재 일자 i에서의 일을 수행하고 난 뒤, 
        #  해당 작업의 소요 기간(tmp[i][0])만큼 미래로 이동한 일자 
        #  i+tmp[i][0]에서 얻을 수 있는 최대 이익

        # tmp[i][1] + dp[i+tmp[i][0]]: 앞 요일 두 개를 합친 값
        # dp[i+1]: 현재까지의 최댓값 (for문은 뒤 인덱스부터 수행되었음)

        # max(상담 진행할 경우의 이득, 하지 않을 경우의 이득)
        dp[i] = max(tmp[i][1] + dp[i+tmp[i][0]], dp[i+1])
        # print(tmp[i][1], dp[i+tmp[i][0]], dp[i+1])
        # print(tmp[i][1] + dp[i+tmp[i][0]], dp[i+1])
        # print('~')
    else:
        dp[i] = dp[i+1]
        # print('@')

    # print(dp)

print(dp[0])