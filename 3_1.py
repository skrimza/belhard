first_par = input('Введите предложение: ')
print(first_par.replace(' ', '-'))

second_par = input('Введите новое предложение: ')
print('-'.join(second_par.split(" ")))
# first exercise