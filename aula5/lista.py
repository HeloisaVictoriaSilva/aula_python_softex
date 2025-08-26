#lista = []
#fatiamento: lista[0:3] # Pega os elementos da posição 0 até a 2
#lista pode ser ordenado e modificada
#variavel = [itens]
#lista.insert(_)= adicionar um elemento em uma lista(2, "laranja")  # Adiciona "laranja" na posição 2
#lista.append() = adicionar um elemento no final da lista
#lista.copy = copiar uma lista

###adicioonar elementos em uma lista
frutas = ["limão", "maça", "morango", "uva"]
frutas.insert(1, "laranja")  
print(frutas)

frutas_vermelhas = ["morango", "creja", "amora", "fraboesa"]

frutas += frutas_vermelhas #adiciona os elementos da lista frutas_vermelhas na lista frutas

###remover elementos de  uma lista
#lista.remove("nome do dado") # Remove o primeiro elemento com o valor do dado
#lista.count("nome do dado") # Conta quantas vezes o dado aparece na lista
#lista.pop() # Remove o último elemento da lista e retorna o valor removido
#del = remove dados da memoria
#lista dentro de outra lista: lista = [[1,2,3]]
# frutas.remove("morango") 
# print(frutas)

# print("primeiro pop")
# frutas.pop()  # Remove o último elemento da lista e retorna o valor removido
# print(frutas)

# print("segundo pop")
# frutas.pop(4) # Remove o elemento na posição 4 e retorna o valor removido
# print(frutas)

# del frutas # Remove a lista inteira da memória
# del frutas[5]  # Remove o elemento na posição 5, mas a lista ainda existe

# frutas2 = frutas[:]  # Cria uma nova lista com todos os elementos de frutas

###copia de lista
#id = identifica o local na memoria onde a lista esta armazenada ou o dado -> id(dado)
# numeros = [3, 5, 7, 9]
# numero2 = numeros

# numeros.append("42")

###copia de lista
# frutas2 = frutas[:] #copiando os elementos da lista
# frutas2 = frutas.copy()

# frutas.clear() #limpa todos os dados de uma lista, tansformando em uma lista vazia
# frutas.extend() # adiciona varios elementos de uma vez no final da lista
# frutas.index("morango") # retorna o índice do primeiro elemento com o valor especificado
# frutas.sort() # Ordena os elementos da lista em ordem crescente
# frutas.reverse() # Inverte a ordem dos elementos na lista

# sorted(frutas) # Retorna uma nova lista ordenada, sem modificar a original, é uma função do python
#list comprehension:
#Uma forma de gerar uma lista com uma sequencia, iteravel ou repetindo valores em apenas uma linha
# é usando o for:
frutas = []
for num in range(10):
    frutas.append(num)
print(frutas)
#Com condicionais:
frutas = []
for num in range(10):
    if num % 2 == 0:
     frutas.append(num)
print(frutas)
#Usando list comprehension:
frutas = [num for num in range(10)]
print(frutas)

frutas_vermelhas = [num for num in range(10) if num % 2 == 0]
print(frutas_vermelhas)