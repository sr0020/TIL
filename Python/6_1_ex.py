# user_input_a = input("정수 입력 > ")

# # 1. if 조건문으로 실행하는 예외처리
# # 사용자 입력이 숫자로만 구성되어 있는 경우
# if user_input_a.isdigit():
#     number_input_a = int(user_input_a)
#     print("원의 반지름: ", number_input_a)
#     print("원의 둘레: ", 2 * 3.14 * number_input_a)
#     print("원의 넓이: ", 3.14 * number_input_a * number_input_a)

# else:
#     print("정수를 입력하지 않았습니다.")

# # 2. try catch 구문으로 실행하는 예외처리
# try:
#     number_input_a = int(user_input_a)
#     print("원의 반지름: ", number_input_a)
#     print("원의 둘레: ", 2 * 3.14 * number_input_a)
#     print("원의 넓이: ", 3.14 * number_input_a * number_input_a)

# except:
#     print("정수를 입력하지 않았습니다.")

# # 3. try except else 구문
# try:
#     number_input_a = int(input("정수 입력> "))
# except:
#     print("정수를 입력하지 않았습니다.")
# else:
#     print("원의 반지름: ", number_input_a)
#     print("원의 둘레: ", 2 * 3.14 * number_input_a)
#     print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
# finally:
#     print("무조건 실행합니다.")

# # 4. try except 구문 사용 파일처리
# try:
#     file = open("info.txt", "w")
#     예외.발생()
# except:
#     print("오류가 발생하였습니다.")
# finally: # finally 없을 시 file closed: false 처리 됨
#     file.close()

# print("file.closed: ", file.closed)

# # 5. try 구문 내부에서 return 키워드를 사용하는 경우
# try에서 return 되엇기 때문에 에러가 발생하지 않아도 else 구문은 출력되지 않는다.
def test(filename, text):
    print("test() 함수의 첫 줄입니다.")
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        file.close()
        print("file.closed: ", file.closed)
        
test("test.txt", "안녕!")
