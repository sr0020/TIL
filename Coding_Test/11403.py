# 0925 1:47 ~ 1:57, 10:20 ~ 10:53
# 접근방식 플로이드-와샬

n = int(input())
m = []

for _ in range(n):
    m.append(list(map(int, input().split())))

# 플로이드-와샬 알고리즘 이용 인접행렬 구하기 (패턴 외우기)
for k in range(n): # k는 중간 정점 (i에서 j로 가는 경로에서 중간 정점 k를 거친다)
    for i in range(n):
        for j in range(n):
                if m[i][k] == 1 and m[k][j] == 1:
                    m[i][j] = 1

# 결과 출력
for i in m:
    for j in i:
        print(j, end=" ")

    print()