PI = 3.141592

def number_input():
    output = input("> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# main 함수(7_3_ex.py) 호출 시 모듈에서 출력하는 코드까지 출력됨
print("모듈의 __name__ 출력하기")
print(__name__)
print()

# 현재 파일이 엔트리 포인트인 경우에만 출력되는 코드 (현재 파일: test_module.py는 엔트리 포인트가 아님. 아래 코드는 출력되지 않음)
if __name__ == "__main__":
    print(get_circumference(10))
