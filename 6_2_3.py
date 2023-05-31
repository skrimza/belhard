def recurs_string(inp):
    if len(inp) == 0:
        return inp
    else:
        return recurs_string(inp[1:]) + inp[0]

res = recurs_string(input('text: '))
print(res)