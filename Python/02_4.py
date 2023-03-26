# 10 format
string_a = "{}".format(10)

print(string_a)
print(type(string_a))

# 5칸 잡고 뒤부터 숫자 넣고 남은 칸은 0으로 처리
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print(output_d, output_e)

output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

output_j = "{:+5d}".format(52)
output_k = "{:+5d}".format(-52)
output_l = "{:=+5d}".format(52)
output_m = "{:=+5d}".format(-52)
output_n = "{:+05d}".format(52)
output_o = "{:+05d}".format(-52)

print(output_f, '\n', output_g, '\n',output_h, '\n', output_i)
print(output_j, '\n', output_k, '\n',output_l, '\n', output_m, '\n',output_n, '\n', output_o)

output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_b)