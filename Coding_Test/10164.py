# 0918 19:40 ~ 20:20, 0919 10:12 ~ 10:55, 0922 1:20 ~ 2:25
# 1번에서 출발한 로봇이 8번 칸을 무조건 지나쳐 15번 칸에 도달하는 경우의 수
# 조건: 오른쪽에 인접한 칸 or 아래에 인접한 칸으로만 이동 가능
# 모든 칸들은 1부터 n*m까지 숫자 순서대로 채워짐

# 풀이방법
# 첫 행, 첫 열을 1로 채우고, 
# 빈칸을 왼쪽, 위쪽 칸의 덧셈 결과로 채우기

# n*m 행렬(행, 렬), k = 무조건 지나쳐야 하는 칸의 수
# 예시 3, 5, 8
n, m, k = map(int, input().split())

# dp 초기화
dp = [[0] * (m) for _ in range(n)] # n행 m열 dp테이블

# dp 수행 (k값이 0이라 모든 칸을 지나야 하는 경우)
if (k == 0):
    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0):
                dp[i][j] = 1
            # 빈칸을 왼쪽, 위쪽 칸의 덧셈 결과로 채우기
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    # 최종 결과
    print(dp[n-1][m-1])
    # print(dp)

# k값이 0이 아니라 k 지점부터 n*m까지의 dp를 구하는 경우
else:
    # k = 8인 경우, (1, 2). 
    # 무조건 지나야 하는 지점의 위치를 구하는 코드임
    x = (k-1) // m # 1
    y = (k-1) % m # 2
    # print(x, y)

    # 1번부터 k지점까지의 경로
    for i in range(x+1):
        for j in range(y+1):
            if (i == 0 or j == 0):
                dp[i][j] = 1
            # 빈칸을 왼쪽, 위쪽 칸의 덧셈 결과로 채우기
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    # 중간지점부터 n*m번 까지의 경로
    for i in range(x, n):
        for j in range(y, m):
            if (i == 0 or j == 0):
                dp[i][j] = 1
            # 빈칸을 왼쪽, 위쪽 칸의 덧셈 결과로 채우기
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    # 최종 결과
    print(dp[n-1][m-1])
    # print(dp)