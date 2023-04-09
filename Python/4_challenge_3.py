# arr = "ctacaatgtcagtatacccattgcattagccgg"
result = {}
div_size = 3

arr = input("> ")

for i in range(0, len(arr), div_size):
    if i in result:
        result[arr[i:i+div_size]] += 1
    elif len(arr[i:i+div_size]) <= 2:
        pass
    else:
        result[arr[i:i+div_size]] = 1

print(result)