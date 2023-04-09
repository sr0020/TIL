
# 1 (2차원 리스트까지 평탄화 가능한 코드)
def flatten(data):
    output = []

    for item in data:
        if type(item) == list:
            output += item # [1, 2, 3], [4, [5, 6]], 7, [8, 9]를 각각 output 리스트에 추가 (=extend())
            print('list = ', item)

        else:
            output.append(item)
            print('element = ', item)

    return output

arr = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(flatten(arr))

# 2 (재귀함수 호출)
# def flatten(data):
#     output = []

#     for item in data:
#         if type(item) == list:
#             output += flatten(item)

#         else:
#             output.append(item)

#     return output

# arr = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print(flatten(arr))