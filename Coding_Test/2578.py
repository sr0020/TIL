# 1029: 11:00 ~ 11:25
# 1106: 9:40 ~ 9:55, 2:00 ~ 2:35
# 1107: 9:10 ~ 9:35
# 1108: 9:15 ~ 9:30
# 1111: 2:10 ~ 2:25

user = []
mc = []
cnt = 0 # 결과값 담을 변수

# input
for _ in range(5):
    a = list(map(int, input().split()))
    user.append(a)

# 빙고 경우의 수 2차원 배열로 저장 (가로빙고, 세로빙고, 대각선)
bingo1 = user
bingo2 = [list(x) for x in zip(*user)]
bingo3 = []
bingo4 = []
for i in range(len(bingo1)):
    bingo3.append(bingo1[i][i])
    bingo4.append(bingo2[4-i][i])

bingo = []
bingo = bingo1 + bingo2 # 2차원 배열 (append 하면 3차원 배열돼서 최종결과 다르게 나옴)
bingo.append(bingo3)
bingo.append(bingo4)

# 몇 번째 수를 부른 후 빙고를 외칠지 출력 
# mc변수를 1차원 리스트로 선언 (i가 1차원 리스트가 아닌 요소로 나와야 하기에)
for _ in range(5):
    mc += list(map(int, input().split()))

# mc 배열 안의 요소가 bingo 변수와 일치하는지 확인
for i in mc:
    cnt += 1
    n = 0 

    for j in bingo: # j가 1차원 리스트
        if i in j:
            j.remove(i)
        if j == []:
            n += 1 # remove 된 후 빈 리스트가 된 경우 빙고 처리

    if n >= 3:
        break

print(cnt)