# 4:10 ~ 4:40
# 4:40 ~ 4:55 (결과 자료형에 문제 있었음)

# 정렬, 문자열
n, m = map(int, input().split())
tmp_hear = []
tmp_see = []

# 듣도 못한 사람의 이름
for _ in range(n):
    hear = input()
    tmp_hear.append(hear)

# 보도 못한 사람의 이름
for _ in range(m):
    see = input()
    tmp_see.append(see)

# # 사전 순 정렬
# tmp_hear = sorted(tmp_hear)
# tmp_see = sorted(tmp_see)

# 중복되는 문자(듣, 보) 새 리스트에 담은 후, 해당 리스트 출력
tmp_hear = set(tmp_hear)
tmp_see = set(tmp_see)

# 사전 순 정렬
# result = tmp_hear.intersection(tmp_see)  # set타입으로 결과값 도출하면 오답처리
result = sorted(list(tmp_hear & tmp_see)) # list

# result
print(len(result))
for i in result:
    print(i)