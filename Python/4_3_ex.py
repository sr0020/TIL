# 1
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print('{}번째 반복: {}'.format(i, array[i]))

print()

# 2
output = ""
for i in range(1, 10):
    output += ("*" * i) # 초기화
    output += "\n"

print(output)

# 3
import time

# 유닉스 타임 개념 참고사이트 - https://www.daleseo.com/python-time/
print(time.time()) # Unix timestamp을 소수로 리턴. 정수부는 초단위이고, 소수부는 마이크로 초단위

number = 0

target_tick = time.time() + 5 
while time.time() < target_tick:
    # print(number)
    number += 1

# 5초 동안 정지 후 반복한 시간 출력
# 컴퓨터의 성능과 상황에 따라 반복 횟수는 다름
# 통신할 때 사용되는 코드
print("5초 동안 {}번 반복했습니다.".format(number))