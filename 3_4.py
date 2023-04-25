a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))
a_pos = a > 0
b_pos = b > 0
c_pos = c > 0
res_pos = a_pos + b_pos + c_pos
a_neg = a < 0
b_neg = b < 0
c_neg = c < 0
res_neg = a_neg + b_neg + c_neg
print(res_pos)
print(res_neg)

