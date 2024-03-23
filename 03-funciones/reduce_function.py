from functools import reduce

numeros = [1, 2, 3, 4, 5]


total = reduce(lambda x,y: x + y, numeros)
print(total)