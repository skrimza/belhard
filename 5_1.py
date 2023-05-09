i = 0
n = int(input('сколько вывести: '))
m = int(input('кратность: '))
k = int(input('левая граница: '))

while i < n:
    k += 1 
    if k % m == 0:
        print(k)         
        i += 1 
