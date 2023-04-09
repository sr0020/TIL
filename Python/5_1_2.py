def mul(*values):
    result = 1
    
    for value in values:
        result *= value

    return result

print(mul(5, 7, 9, 10))