# 선택정렬
# arr의 원소 중 가장 작은 원소를 가진 인덱스를 찾고 이를 arr 앞지리부터 교환

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 탐색 후 제일 작은 인덱스 찾기
for i in range(len(arr)):
    min_index = i #
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    # 정렬 (요소 값 변경)
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)