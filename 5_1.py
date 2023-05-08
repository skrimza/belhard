i = 0
n = int(input('сколько вывести: '))
m = int(input('кратность: '))
k = int(input('левая граница: '))
numbers = []

while not i:
    i += 1
    if i > k and i % m == 0:
        numbers.append(i)
        if len(numbers) > n:
            break  
print(numbers)