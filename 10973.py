# 0904 1:15 ~ 1:40, 10:55 ~ 11:15
# 이전 순열

n = int(input())
m = list(map(int, input().split()))
flag = 0

# 오른쪽(뒤)부터 오름차순 발생하는지 확인 (내림차순 깨지는지 확인)
for i in range(n-1, 0, -1):
    if m[i] < m[i-1]:
        print(i-1, m[i-1], ' ', i, m[i])

        # 오름차순 발생하는 경우 (깨진 위치보다 '오른쪽'에서부터 0까지 순회)
        for j in range(n-1, 0, -1):
            # print(j)

            # 변경 target으로 하고 있는 요소와 해당 요소보다 작은 숫자 자리 change
            # ex) 5 4 1 2 3에서 target: 4, 해당 요소보다 작은 숫자: 3 => 자리 change
            # 자리 change된 상태에서, i번째 요소 (위 ex에서 3) 뒤의 숫자는 내림차순 정렬
            if m[j] < m[i-1]: # 순회하다가 오름차순 발견되는 경우
                print(i-1, m[i-1], ' ', j, m[j])
                m[i-1], m[j] = m[j], m[i-1]

                # 바로 이전 순열을 찾아야 하므로, m[:i] 뒤는 내림차순 정렬
                m = m[:i] + sorted(m[i:], reverse=True)
                # print(m[:i])
                print(*m)
                exit(0)


# 내림차순 없는 경우 -1 출력
print(-1)