# 0906 1:45 ~ 1:55
# 0916 5:05 ~ 5:35
# 문자열 그리디

# 식의 값을 '최소'로 만드는 프로그램
s = input().split('-')
# print(s)
sum = 0

# +는 무조건 더하고
for i in s[0].split('+'):
    sum += int(i)

# print(sum)

# 최초로 -가 나올 때부터 모두 빼주는 방식
# 55-50+40과 55-(50+40)은 동일하고, 이 55-(50+40)가 최솟값
for i in s[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)