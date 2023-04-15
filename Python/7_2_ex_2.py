def test(function): # 1
    def wrapper(): # 3 6
        print("인사가 시작되었습니다.") # 7
        function()
        print("인사가 종료되었습니다.") # 9

    return wrapper # 4

@test # 2
def hello(): 
    print("hello") # 8 

hello() # 5

# 데코레이터 함수인 test는 함수를 인자로 받습니다.
# @test 데코레이터를 통해 hello 함수를 test 함수의 인자로 전달합니다.
# wrapper 함수는 hello 함수를 실행하기 전과 후에 인사가 시작되었습니다.와 인사가 종료되었습니다.를 출력합니다. (hello 함수 호출 전이라, 이 위치에서 wrapper 함수가 직접 실행되지는 않음.)
# wrapper 함수를 리턴합니다.
# hello 함수가 호출됩니다. (hello 함수는 test의 함수의 function 인자로 전달된 상태고, test 함수가 호출됨)
# wrapper 함수가 호출됩니다.
# 인사가 시작되었습니다.를 출력합니다.
# function 인자로 전달된 hello 함수가 실행됩니다.
# hello 함수 내부에서 hello를 출력합니다.
# 인사가 종료되었습니다.를 출력합니다.

# 즉, 위 코드는 hello 함수를 실행하기 전과 후에 인사말을 출력하는 데코레이터를 구현한 예시입니다.