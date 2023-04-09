# 2차원 평탄화
def flatten(a):

    result = []

    for i in a:
        if type(i) == list:
            result += flatten(i) # 리스트의 데이터가 리스트일 때 (else 조건문 충족 시까지)재귀함수로 들어가서 result에 int형 element로 담기
        else:
            result.append(i)

    return result

arr = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
result = flatten(arr)

print(f"{arr}를 평탄화하면\n{result}입니다.")