# n, m, k = 배열, 더해지는 수의 갯수, 연속해서 더해질 수 있는 갯수

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# print(first, second)

result = 0

# print(k)

while True:
    for i in range(k):
        if m == 0:
            break;
        result += first

        m -= 1

    if m == 0:
        break;
    result += second
    m -= 1

print(result)