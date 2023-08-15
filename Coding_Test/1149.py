# 2:00 ~ 4:00
"""
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 하며,
n번 집의 색은 n-1번의 집 색과 같지 않아야 한다.

그리디로 풀려했고, 접근이 좀 어려웠음
기존에 한 번도 생각해 본 적 없는 방식으로 풀게 됨
"""

n = int(input())
rgb = [0] * n

for i in range(0, n):
    rgb[i] = list(map(int, input().split()))

# 1. i번째 r, g, b 값을 
# 2. 이전 값의 최솟값과 더한 값을 r, g, b별로 구하고,
# 3. 최종적인 r, g, b 결과값을 나타내는 n-1번째 인덱스에서 r, g, b 중 최솟값 구하기
# * 연속해서 같은 색상이 올 수 없음.
for i in range(1,n): 
    rgb[i][0]= min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0]
    rgb[i][1]= min(rgb[i-1][0],rgb[i-1][2]) + rgb[i][1]
    rgb[i][2]= min(rgb[i-1][0],rgb[i-1][1]) + rgb[i][2]

    # print()
    # print(i, rgb[i][0], rgb[i][1], rgb[i][2])

print(min(rgb[n-1])) # n으로 하면 indexerror 뜸