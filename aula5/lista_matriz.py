#Listras bidimensionais são matrizes. No python isso quer dizer uma lista que
#comtem outas listas formando uma matriz no formato número_listax número_itens
#1D → lista simples
#2D → matriz (linha × coluna)
#3D → lista de matrizes (bloco × linha × coluna)
#exemplo de uma matriz 2x2:
matriz = [[1,2], [3,4]]
#também pode ser representada assim:
matriz = [[1,2]
           [3,4]]

matriz3x3 = [[1,2,"a"]
             [3,4,"b"]
             [5,6,"c"]]

#matriz com list comprehesion:
matriz= [[i for i in range(3)] for x in range(3)] 
#[i for i in range(3)] → cria uma lista [0, 1, 2]
#  for x in range(3)] e repete essa lista 3 vezes
# criando uma matriz em uma unica linha matriz == [[0, 1, 2], [0, 1, 2], [0, 1, 2]] 
matriz2= [] #cria uma lista vazia
for i in range(3): #o laço roda 3 vezes
    sublista = [] #cria uma nova lista vazia
    matriz.append(sublista) #anexa essa sublista em matriz
    for x in range(3): # preenche sublista com 0,1,2
        sublista.append(x) # adiciona 0,1,2 na sublista
print(matriz)
#saida do terminal: 
#matriz == [[0,1,2],[0,1,2],[0,1,2], [0,1,2],[0,1,2],[0,1,2]]

matriz = [[1,2,3], #linha 0
          [4,5,6], #linha 1
          [7,8,9]] #linha 2
matriz[1][2] = "a" #[1]: acessa a segunda linha | [1][2]: acessa a coluna de índice 2 
#dessa linha (o valor 6), subistituindo po "a"
print(matriz)

#lista tridimensional: Uma lista tridimensional é basicamente uma lista dentro de uma lista dentro de outra lista.
# Ela tem três níveis de profundidade, assim como uma tabela 3D: linhas × colunas × “camadas”.
#1ª dimensão → pode representar, por exemplo, blocos de um condomínio.
#2ª dimensão → dentro de cada bloco, pode representar andares.
#3ª dimensão → dentro de cada andar, representa apartamentos.
condominio = [
    [["A1","A2","A3"],["A4","A5","A6"],["A7","A8","A9"]], # bloco A
    [["B1","B2","B3"],["B4","B5","B6"],["B7","B8","B9"]], # bloco B
    [["C1","C2","C3"],["C4","C5","C6"],["C7","C8","C9"]]] # cloco C

print(condominio[1][0][2]) 
# [1]: escolhe o segundo bloco, bloco B
# [0]: primeiro andar
# [2]: terceiro apartamento -> "B3"