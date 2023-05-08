number = input('Введите число: ')
max_i = 0

for i in number:
    if i.isdigit() and int(i) > max_i:
        max_i = int(i)

print(f"Максимальная цифра в числе {number} равна {max_i}")