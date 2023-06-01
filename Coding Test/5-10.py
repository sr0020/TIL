# 음료수 얼려 먹기
# 한 번 더

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input()))) # list int형태로 받아야 함.

def dfs(x, y):
    # 예외처리
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 방문 처리
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True
    return False

# 아이스크림 만들기
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)