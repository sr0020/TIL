# 염기 서열 중 각각의 염기가 몇 개 포함되어 있는지 세는 프로그램 구현

# arr = "ctacaatgtcagtatacccattgcattagccgg"

arr = input('> ')
result = {}

for s in arr:

    if s in result:
        result[s] += 1        
    else:
        result[s] = 1

# print(result)

for i in result:
    print("{}의 개수: {}".format(i, result[i]))