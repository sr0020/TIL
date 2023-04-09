# 100 명의 사람이 하나 이상의 테이블에 나누어 앉는 패턴의 경우의 수
min_num = 2 # 앉힐 수 있는 최소의 사람 수
max_num = 10 # 앉힐 수 있는 최대의 사람 수
all_num = 6 # 전체 인원 수 (6명. 임시)
memo = {}

def sol(remain, done): # 남은 사람 수, 앉힌 사람 수
    key = str([remain, done])
    result = 0

    # 종료 조건
    if key in memo:
        return memo[key]

    if remain < 0:
        return 0

    if remain == 0:
        return 1

    # 재귀 처리
    for i in range(done, max_num + 1):
        # print('remain-i = {}, i = {}, remain = {}, done = {}'
        #       .format(remain-i, i, remain, done))
        result += sol(remain-i, i)

    # 메모화 처리
    memo[key] = result
    print(memo)

    # 종료
    return result # result = 경우의 수

print(sol(all_num, min_num))