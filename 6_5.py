def reverse_list():
    listen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    while i < len(listen):
        del_elem = listen.pop()
        listen.insert(i, del_elem)
        i += 1
    print(listen)

reverse_list()
