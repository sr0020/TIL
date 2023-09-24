# 0922 2:41 ~ 2:50, 
# 0923 3:30 ~ 4:40
# 0924 2:50 ~ 3:50

t = int(input()) # 테스트케이스의 수

for _ in range(t):
    # 문서의 갯수, 원하는 문서가 몇 번째(인덱스)에 있는지
    # * 인덱스는 0부터 시작함.
    n, m = list(map(int, input().split())) 

    # N개 문서의 중요도 (높은 순서대로 우선순위 가짐)
    k = list(map(int, input().split()))

    count = 0
    idx = [i for i in range(n)]
    idx[m] = 'target'

    # 알고리즘
    # 배열이 k, idx 이렇게 두 개 있음
    while k:
        # max값이 0번째 인덱스에 오면 count++
        if k[0] == max(k):
            count += 1

            # idx에 가장 중요도 낮은 인덱스가 오면 결과값 print
            # 바로 위 if문의 조건이 충족되는 경우, 
            # idx[0]이 1이 될 때까지 k.pop(0), idx.pop(0)
            if idx[0] == 'target':
                print(count)
                break

            k.pop(0) # 0번째 인덱스 무조건 pop
            idx.pop(0)

            # print(k, idx)

        # max값이 0번째 인덱스에 오지 않는 경우, 
        # 원 배열에서 pop 후 이어붙이기
        else:
            k.append(k.pop(0))
            idx.append(idx.pop(0))

            # print(k, idx)