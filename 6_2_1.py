# writing a function-generator with three arguments
# (number, start, stop) all arguments is integer. 
# the generator should return a number in the power from start to end
# for example:
# number=2
# start=3
# end=5
# result: 8, 16, 32

def square_number(number, start, stop):
    for i in range(start, stop+1):
        yield number ** i

res = square_number(2, 3, 5)
print(f'result: {next(res)}, {next(res)}, {next(res)}')
