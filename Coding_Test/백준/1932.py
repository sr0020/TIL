# 0803 - 10:30 ~ 11:40, 12:20 ~ 1:30
# 0804 - 11:50 ~ 13:05
# 선택된 수의 합이 최대가 되는 경로 구하기 (최댓값 출력)

# 아래층에 있는 수는 현재 층에서 선택된 수의 
# 대각선 왼, 오른쪽에서만 선택 가능
# 30: 7 + 3 + 8 + 7 + 5

"""
그리디로 푸는 습관 고치기
당장의 최적해가 아니라, 
부분 문제 해결 후 이를 조합해 전체 문제를 해결하는 게 정답

dp 테이블 각 자리별로 이전 값들의 합이 들어 옴
"""

result = 0
n = int(input())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split())) # 줄 마다 입력

# * 0열, 마지막 열에 오는 화살표는 대각선 방향 없이 1개
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            a[i][j] += a[i-1][j]
        elif j == i:
            a[i][j] += a[i-1][j-1]
        else:
            a[i][j] += max(a[i-1][j-1], a[i-1][j])

    # print(a[i])
    # print(max(a[i]))
    # print()

print(max(a[n-1]))