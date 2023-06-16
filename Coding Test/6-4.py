# 퀵 정렬

def quick_sort(arr):

    # 원소가 한 개인 경우
    if len(arr) <= 1:
        return arr

    # 피봇 설정 (가장 왼쪽 숫자)
    pivot = arr[0]
    smaller = []
    greater = []

    for k in range(1, len(arr)): # for k in range(len(arr)) => recursion 오류 (불필요한 반복 실행)
        if arr[k] <= pivot:
            smaller.append(arr[k]) # 인덱스 순서 상관없이 pivot보다 작은 요소
        else:
            greater.append(arr[k]) # 인덱스 순서 상관없이 pivot보다 큰 요소

    # print("smaller = ", smaller, ', k = ', k, ", pivot = ", pivot)
    # print("greater = ", greater, ', k = ', k, ", pivot = ", pivot)
    # print()

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

# main
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
result = quick_sort(arr)
print('Result = ', result)
print()


# ### 함수 부분 이전 코드 (1회전)

# def quick_sort(arr):
    
#     # 원소가 한 개인 경우
#     if len(arr) <= 1:
#         return arr

#     # 피봇 설정 (가장 왼쪽 숫자)
#     pivot = arr[0]
#     smaller = []
#     greater = []

#     for k in range(len(arr)):
#         # step 1
#         # 왼쪽부터 피봇보다 큰 숫자 찾기
#         for i in range(0, len(arr)):
#             if arr[i] > pivot:
#                 # print('i = ', i, ', arr[i] = ', arr[i])
#                 big = i
#                 break

#         # 오른쪽부터 피봇보다 작은 숫자 찾기
#         for i in reversed(range(len(arr))):
#             if arr[i] < pivot:
#                 # print('i = ', i, ', arr[i] = ', arr[i])
#                 small = i
#                 break

#         # print('Big = ', big, 'Small = ', small)

#         # step 2
#         # 두 값이 엇갈린 경우 (인덱스 상 big이 small보다 뒤에 있는 경우)
#         if big > small:

#             # small과 pivot을 교환
#             arr[small], arr[0] = arr[0], arr[small] # step 3: partition
#             break

#         # 둘이 swap
#         arr[big], arr[small] = arr[small], arr[big]

#     return arr