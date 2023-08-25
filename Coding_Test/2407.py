# 0825 1:18 ~ 1:21

n, m = map(int, input().split())

def fac(n):
    fac = 1

    for i in range(1, n+1):
        fac *= i

    return fac

result = fac(n) // (fac(m) * fac(n-m))
print(result)