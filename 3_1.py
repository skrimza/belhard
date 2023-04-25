first_par = input('Введите предложение: ')
print(first_par.replace(' ', '-'))

second_par = input('Введите новое предложение: ')
sec_change = second_par.split(" ")
print('-'.join(sec_change))
# first exercise