# import collections

# text = input('Введите произвольный текст: ')
# data = collections.Counter(text)
# print(data)

sum_text = list(input('Введите новое предложение: '))

# sym = {i: sum_text.count(i) for i in sum_text}
# print(sym)

sym = {}
sym.update({i: sum_text.count(i) for i in sum_text})
print(sym)