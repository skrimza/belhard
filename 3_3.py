first_name = input('Введите ваше имя: ')
age = input('Введите ваш возраст: ')
city = input('Введите ваш город: ')
f_example = '''Здравствуйте, %(first_name)s.
Ваш возраст %(age)s лет, и вы родом из %(city)s.
Желаем вам хорошего дня!''' % {'age': age, 'first_name': first_name, 'city': city}
sec_example = '''Здравствуйте, {}. Ваш возраст {} лет,
и вы родом из {}. Желаем вам хорошего дня!'''.format(first_name, age, city)
third_example = f'''Здравствуйте, {first_name}. Ваш возраст {age} лет,
и вы родом из {city}. Желаем вам хорошего дня!'''
print(f_example)
print(sec_example)
print(third_example)