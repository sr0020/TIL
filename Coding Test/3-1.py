n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 거스름돈
    n %= coin

    print('---')
    print(count)
    print(n)
    print(coin)
    print('---')

print("result = ", count)