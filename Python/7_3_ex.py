# 1. 모듈
import test_module as test

print("메인의 __name__ 출력하기")
print(__name__)
print()

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))
print()
print()

# # 2-1. 패키지
# import test_package.module_a as a
# import test_package.module_b as b

# print(a.var_a)
# print(b.var_b)

# print()
# print()

# 2-2. 패키지 전체 불러오기
# __init__.py 파일을 가장 먼저 실행시킴
from test_package import *
print(module_a.var_a)
print(module_b.var_b)
print()
print()