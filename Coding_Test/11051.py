# 0825 12:45 ~ 1:14

# 조합 공식(n! / k! * (n-k)!)만 알면 바로 풀리는 문제
# + 여타 응용문제들도 그 속에서 공식만 찾아내면 풀이 수월해짐 

n, k = map(int, input().split())
dp = [0] * 1001
# print(n, k)

# fac 구현
def fac(n):
    fac = 1

    for i in range(1, n+1):
        fac *= i
        # print(fac)

    return fac

result = (fac(n) // (fac(k) * fac(n-k))) % 10007
print(result)