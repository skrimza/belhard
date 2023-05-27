listen = [123, True, 'Hello', [1, 2, 3], 'Python']
listen = list(filter(lambda x: type(x) == str, listen))
print(listen)