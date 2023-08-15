# 2:20 ~ 3:15
# 조합 문제
# 문제 이해가 핵심인 문제
def func(n):

    fac = 1
    
    # 팩토리얼 구현
    for i in range(1, n+1):
        fac *= i

    return fac

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # n, m 값에 유의
    # 동쪽의 다리(m)가 서쪽의 다리(n) 갯수보다 큼.
    # mCn으로 표현됨.
    # + 분모값부터 계산되게 식 설정
    result = func(m) // (func(m-n) * func(n))
    print(result)
