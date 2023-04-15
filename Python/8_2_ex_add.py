class CustomException(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message = message
        self.value = value

    def __str__(self):
        return self.message
    
    def print(self):
        print(self.message)
        print(self.value)

try:
    raise CustomException("사용자 정의 예외 클래스", 273)
except CustomException as e:
    e.print()