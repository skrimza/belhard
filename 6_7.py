# * Дан список чисел, необходимо для каждого элемента 
# посчитать сумму его соседей, для крайних чисел 
# одним из соседей является число с противоположной
# стороны списка

def sum_numbers():
    listen = [1, 2, 3, 4, 5, 6, 7]
    diction = {}
    for i in range(len(listen) - 1):
        diction.update({listen[i]: (listen[i-1]+listen[i+1])})
    else:
        diction.update({listen[i+1]: (listen[i]+listen[0])})
    print(diction)
    # return ({listen[i]: (listen[i-1] + listen[i+1]) 
    #          for i in range(len(listen)-1)})
sum_numbers()

