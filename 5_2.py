f_num = float(input('Введите первое число: '))
symb = input('Введите знак(+, -, *, /): ')
s_num = float(input('Введите второе число: '))
res = 0
while not res:
    if symb == '+':
        res = f_num + s_num
    elif symb == '-':
        res = f_num - s_num
    elif symb == '*':
        res = f_num * s_num
    elif symb == '/':
        res = f_num / s_num
print(res)