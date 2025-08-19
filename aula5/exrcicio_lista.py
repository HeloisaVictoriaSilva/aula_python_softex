#exercicio1
dados_diferentes = [1,56,68, "azul", "ferro", "radio", 2.8, 7.9 ]
print(dados_diferentes)

#exercicio2 
dados_diferentes.append("polonio")
dados_diferentes.insert(5, 2.7)
print(dados_diferentes)

#exercicio3
dados2 = dados_diferentes[:]
dados3 = dados2.copy()
print(id(dados_diferentes))
print(id(dados2))
print(id(dados3))
print(dados2)
print(dados3)

#exercicio4
numeros = [1,65,7.8,8.9]
nova_lista = []
for numero in numeros:
    nova_lista.append(numero * 2)

print(nova_lista)

#exercicio5
numeros2 = [1, 2, 3, 4, 5, 6]
lista2 = numeros2[3:5]
print(lista2)
