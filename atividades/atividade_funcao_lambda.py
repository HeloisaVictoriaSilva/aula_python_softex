from functools import reduce
#1
numeros = [1,2,3,4,5]
calcular = list(map(lambda x: x*2, numeros))
print(calcular)

#2
filtrar = [10, 15, 20, 25, 30]
print(list(filter(lambda x: x % 2 == 0, filtrar)))

#3
soma = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, soma))

#4
frutas= ["uva", "banana", "maçã", "laranja"]
ordenacao= sorted(frutas, key= lambda x: len(x))
print(ordenacao)

#5
nomes=  ["ana", "pedro", "maria"]
print(list(map(lambda x: x.capitalize(), nomes)))

#6
numero=  [2, 3, 4, 5]
multiplicar = reduce(lambda x, y: x * y, numero)
print(multiplicar)

#7
fruta= ["banana", "uva", "maçã", "laranja"]
ordenar= sorted(fruta, key= lambda x: x[-1])
print(ordenar)