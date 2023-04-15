import os

def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path) # 매개변수로 들어온 path의 모든 요소 값 불러오기
    print(output)

    # 폴더의 요소 구분하기
    for item in output:
        if [x for x in output if os.path.isdir(item)]: # 여기는 path가 아니라 for문의 인덱스 item이 들어가야 함
            # 폴더라면 계속 읽어 들이기
            read_folder(path + "/" + item)
        else:
            # 파일이라면 출력하기
            print("파일: ", item)

# 현재 폴더의 파일/폴더를 출력합니다.
read_folder(".")