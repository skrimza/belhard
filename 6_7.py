# * the list of numbers is given, need for each element
# calculate the sum neighbour, for extreme numbers, 
# one of the neighbors is an element located on the 
# opposite side

def sum_numbers():
    listen = [1, 2, 3, 4, 5, 6, 7]
    diction = {}
    for i in range(len(listen) - 1):
        diction.update({listen[i]: (listen[i-1]+listen[i+1])})
    else:
        diction.update({listen[i+1]: (listen[i]+listen[0])})
    print(diction)


sum_numbers()

