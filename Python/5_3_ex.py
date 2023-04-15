#
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("Hello")

call_10_times(print_hello)

# 함수
# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

# lambda
# power = lambda x: x*x
# under_3 = lambda x: x < 3

list_input_a = [1, 2, 3, 4, 5]

# map()
# output_a = map(power, list_input_a)
output_a = map(lambda x: x*x, list_input_a)
print(output_a)
print(list(output_a))
print()

# filter()
# output_a = filter(under_3, list_input_a)
output_a = filter(lambda x: x < 3, list_input_a)
print(output_a)
print(list(output_a))
print()

# # file open/write and read
# file = open("basic.txt", "w")
# file.write("Hello Python Programming")
# file.close()

# with open("basic.txt", "r") as file:
#     contents = file.read()
# print(contents)

# file open/write and read
import random
hangul = list("가나다라마바사")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hangul) + random.choice(hangul)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", "r") as file: 
    # print(file): <_io.TextIOWrapper name='info.txt' mode='r' encoding='UTF-8'>
    for line in file:
        (name, weight, height) = line.rstrip().split(", ")

        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / ((int(height) / 100) * 2)
        result = ""

        if 25 < bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print("\n".join([
            "이름: {}",
            "몸무게 : {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))

        print()
