numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    # 1. 3으로 나눈 이유 = 1차원 배열 3개.
    # 2. n + 2를 통해 배열 값이 3 4 5 ~로 되게 만들고
    # 이런 식으로 나눈 값이 0 1 2 순서로 되도록 만들어 줌
    output[(number+2) % 3].append(number)
    # print((number) % 3) # => [1, 2, 0, 1, 2, 0, 1, 2, 0]

print(output)