n, k = map(int, input().split())
cnt = 0

while n > 1:
    # k로 나누어 떨어지는 경우 n // k
    if n % k == 0:
        n //= k # n이 아닌 새로운 변수를 넣어서 대입하는 경우 (ex) result = n // k) while문 새로 돌아갈 때마다 해당 변수가 초기화되는 형식임. 오류 발생
        cnt += 1

    else: 
        n -= 1
        cnt += 1

    # print(n)

print(cnt)