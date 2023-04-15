numbers = list(range(1, 10+1))

print("# 홀수만 추출하기")
print(list(filter(lambda a: a % 2 == 1, numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda a: a >= 3 and a < 7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda a: a**2 < 50, numbers)))
print()