listen = [22, 44, 31, 5, 9, 6, 1, 75, 32, 68]
listen.sort(key=lambda x: not x % 2 == 0)
print(listen)