def f(x):
    return 2*x + 1

def f_2(x):
    return x ** 2 + f(x)

print(f(10))
print(f_2(10))