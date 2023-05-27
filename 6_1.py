# writing a function for convert from decimal into binary
# number and back

def decimal_to_binary(number):
    bin = ' '
    while number > 0:
        bin = str(number % 2) + bin
        number //= 2
    print(bin)
    return sum([2**i for i in range(len(bin)) if bin[::-1][i] == '1']) / 2     

res = decimal_to_binary(563)
print(res)


