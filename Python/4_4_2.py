# 리스트 컴프리핸션
# 
output = [x for x in range(1, 100+1) 
          if "{:b}".format(x).count('0') == 1]

# 
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))

print("합계:", sum(output))