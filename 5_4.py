# first task

# number = input('Введите число: ')
# max_i = 0

# for i in number:
#     if i.isdigit() and int(i) > max_i:
#         max_i = int(i)

# print(f"Максимальная цифра в числе {number} равна {max_i}")

# second task

# num = input('Введите несколько чисел через пробел: ').split(' ')

# for i in num:
#     num = list(map(int, num))
#     res = sum(num) / len(num)
#     print(res)

# third task

from random import randint
a = randint(1, 100)
rand_num = -1
i = 0

while a != rand_num:
    rand_num = int(input('Введите число: '))
    if rand_num < a:
        print('больше')
    elif rand_num > a:
        print('меньше')
    else:
        print('красава')
    i += 1
print(i)