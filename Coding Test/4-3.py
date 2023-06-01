n = input()

row = int(n[1])
column = int(ord(n[0])) - 96

# print(row, column)
result = 0

dx = [2, -2, 1, -1, 2, -2, 1, -1]
dy = [1, -1, 2, -2, -1, 1, -2, 1]

for i in range(len(dx)): # len(n)이 아니라 len(dx)

    nx = row + dx[i]
    ny = column + dy[i]

    # print(nx, ny)

    if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
        continue

    result += len(str(nx))
    # print(nx, ny)

print(result)