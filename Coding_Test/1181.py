# 4:55 ~ 5:22

n = int(input())
temp = []

for _ in range(n):
    s = input()
    temp.append(s)

# 길이가 짧은 원소부터 출력
# result = sorted(temp, key=lambda x: len(str(x)))

# 길이가 같으면 사전 순으로 출력
# result = sorted(temp, key=lambda x: (len(str(x)), x))

# 중복 제거
result = sorted(set(temp), key=lambda x: (len(str(x)), x))

print()

for i in result:
    print(i)

