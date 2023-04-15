# # 모든 예외 잡기
# list_number = [52, 273, 32, 72, 100]

# try:
#     number_input = int(input("정수 입력> "))
#     print("{}번째 요소: {}".format(number_input, list_number[number_input]))
#     예외.발생()
# except ValueError as exception:
#     print("정수를 입력해주세요!")
#     print(type(exception), exception)
# except IndexError as exception:
#     print("리스트의 인덱스를 벗어났어요!")
#     print(type(exception), exception)
# except Exception as exception:
#     print("미리 파악하지 못한 에러가 발생했습니다")
#     print(type(exception), exception)

# raise 구문. 일부러 예외를 발생시켜 프로그램 강제 종료 방지
number = input("정수 입력> ")
number = int(number)

if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError

