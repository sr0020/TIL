def func(input):
    arr = [500, 100, 50, 10, 5, 1]
    result = 0
    init = 1000

    temp = init - input

    for i in arr:
        if temp >= i:
            result += temp // i
            temp %= i

    return result

change = int(input())
print(func(change))