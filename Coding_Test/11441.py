# 0901 11:25 ~ 12:27
# 1. 시간복잡도 o(n^m) => o(m)으로 줄이는 게 관건

import sys # 2 필수
input = sys.stdin.readline

# input
n = int(input()) # 수의 갯수
a = list(map(int, input().split())) # n 크기의 배열
sum = [0] * (n + 1)

# 누적 합 구하기
for i in range(0, n):
    sum[i+1] = sum[i] + a[i] # sum[1] = 10 이런 식으로 담김

# 결과값 계산
m = int(input()) # 구간의 갯수 m
for _ in range(m): # i, j (각 구간을 나타냄)
    i, j = map(int, input().split())

    # j번째 요소 - i-1(시작점 바로 직전값)번째 요소
    result = sum[j] - sum[i - 1]
    print(result)