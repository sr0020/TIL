numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


for i in range(0, len(numbers) // 2):
    j = (i * 2) + 1 # 홀수 출력. numbers 배열 사용 없이 i만 사용
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] ** 2

print(numbers)