# A list containing various types of data is given, filtered in such
# a way that only rows remain, using an additional list
# is illegal
listen = [123, True, 'Hello', [1, 2, 3], 'Python']
listen = list(filter(lambda x: type(x) == str, listen))
print(listen)