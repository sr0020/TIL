# 0902 3:35 ~ 5:35
# 순열 유형 익숙하지 않았고, for문의 i, j가 헷갈렸음

n = int(input())
a = list(map(int, input().split()))

# 뒤에서부터 내림차순이 발생하는지 확인
for i in range(n-1, 0, -1):
    if a[i-1] < a[i]: # 내림차순 발생하는 경우 (= 오름차순이 깨지는 경우)
        # print(a[i-1], a[i])

        # 내림차순 깨진 위치보다 오른쪽에서부터 0까지 리스트 a 순회
        for j in range(n-1, 0, -1):
            # print(a[i-1], a[j])

            # 처음 내림차순 발생하는 경우 숫자 swap 및 다음 순열 출력 후 종료
            # i, j로 검사하는 이유: j로 0 ~ n-1자리의 내림차순 여부를 모두 검사하기 위함
            if a[i-1] < a[j]:
                # print(a[i-1], a[j])
                a[i-1], a[j] = a[j], a[i-1]
                a = a[:i] + sorted(a[i:])
                print(*a)

                exit(0)

print(-1)