# # first task

# number = input('Введите число: ')
# max_i = 0

# for i in number:
#     if i.isdigit() and int(i) > max_i:
#         max_i = int(i)

# print(f"Максимальная цифра в числе {number} равна {max_i}")

# # second task

# num = input('Введите несколько чисел через пробел: ').split(' ')

# for i in num:
#     num = list(map(int, num))
#     res = sum(num) / len(num)
#     print(res)

# # third task

# from random import randint
# a = randint(1, 100)
# i = 1

# while i:
#     rand_num = int(input('Введите число: '))
#     if rand_num < a:
#         print(f'больше, я загадал {a} число')
#     elif rand_num > a:
#         print(f'меньше, я загадал {a} число')
#     else:
#         print('красава')
#         break
#     i += 1
# print(i)

# fourth task

# coins = (25, 10, 5, 1)
# count = 0
# pay = int(input('Введите число:'))

# for coin in coins:
#     count += pay // coin
#     pay -= (pay // coin) * coin
# print(count)


