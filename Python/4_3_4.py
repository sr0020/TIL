max_value = 0
a = 0
b = 0

for i in range(1, 100): # i는 1~100
    j = 100 - i # j는 100부터 거꾸로 내려 옴.

    if (i * j) > max_value:
        max_value = i * j
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))