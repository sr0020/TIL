numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for number in numbers: # number = 요소 값 (인덱스 아님)
    if number in counter:
        counter[number] += 1 # counter[number]의 키 number는 인덱스 0번부터 중복없이 추가됨
        # print('not 1 = ', counter[number])
    else:
        counter[number] = 1
        # print('1 = ', counter[number])

print(counter)