#1
livros =["1984", "percy jackson", "o conto da aia"]
print(livros)

#2
print(livros[0])
print(livros[-1])

#3
livros.append("jogos vorazes") 
livros.append("os crimes ABC")
print(livros)

#4
livros.insert(1,"Duna")
print(livros, "inserindo duna")

#5
print("Livro o silencio dos inocentes não encontrado")

#6
numeros=[1,2,3,2,4,2,5]
print(numeros.count(2))

#7
for livro in livros:
    print("O livro ", livro, " é interessante")

#8
idades=[12,18,25,14,30]
for idade in idades:
     if idade >= 18:
         print(idade)
else:
    pass

#9
soma = 0 
valores=[10, 20, 30, 40]
for valor in valores:
    soma = soma + valor
    print(soma)

#10:
#primeiro aluno
nota_aluno1=[]
for i in range(3):
   nota1= int(input(" informe a nota do primeiro aluno: "))
   nota_aluno1.append(nota1)
#segundo aluno
nota_aluno2=[]
for i in range(3):
   nota2= int(input(" informe a nota do segundo aluno: "))
   nota_aluno2.append(nota2)
#adicionando as notas do primeiro e segundo aluno na lista notas
notas = []
notas.append(nota_aluno1)
notas.append(nota_aluno2)

#organizar a lógica esta errada
contador=0
soma1=0
for aluno in notas:
    for nota in aluno:
         contador +=1
         soma1 = soma1 + nota
    media = soma1 / contador
print(media)
