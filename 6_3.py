# given b list of numbers & number arrives.
# we need to shift this list to specified number
def reversed_list(number):
    listen = [1, 2, 3, 4, 5, 6]
    i = 0
    while i < number:
        elem = listen.pop()
        listen.insert(0, elem)
        i += 1
    print(listen)
        


print(reversed_list(int(input('Введите цифру: '))))