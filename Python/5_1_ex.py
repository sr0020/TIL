#
def test(a, b=10, c=100):
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    print(a + b + c)

test(b=10, c=20, a=30) # 키워드 매개변수 뒤에 일반 매개변수 오면 SyntaxError: positional argument follows keyword argument
test(10, b=30)
