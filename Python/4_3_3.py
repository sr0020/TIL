limit = 10000
i = 1
sum_value = 0

for i in range(i, limit):
    sum_value += i
    print(i, sum_value)
    if sum_value > limit:
        break

print("{}를(을) 더할 때 {}을 넘으며 그때의 값은 {}입니다.".
      format(i, limit, sum_value)) 