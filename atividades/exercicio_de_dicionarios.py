#1
aluno = {
    "nome": "Joaquim",
    "idade": 23,
    "nota": 9.9
}
#2
produto = {
    "nome": "caneta",
    "preco": 2.5,
    "estoque": 100
}
print(f"{produto["nome"]} está com o estoque: {produto["estoque"]}")

#3
aluno["Nome"] = "Carlos"
aluno["Idade"] = 30
aluno["cidade"] = "São Paulo"
print(aluno)

#4
carro = {
    "marca": "Ford",
    "modelo": "Fiesta",
    "ano": 2010
}
carro.pop("ano")
print(carro)

#5
contato = {
    "nome": "Ana",
    "email": "ana@gmail.com",
}
print(contato.get("telefone"))

#6
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
def contador(palavras):
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1   
    return frequencia                 


print(contador(palavras))

#7
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
inverter = {}
for chave, valor in d.items():
    inverter[valor] = chave
print(inverter)

#8
notas_alunos = {
    "Ana": [7, 8, 9],
    "Carlos": [6, 5, 7],
    "Beatriz": [10, 9, 8]
}
for nome, notas in notas_alunos.items():
    soma = 0
    contador = 0
    for nota in notas:
        soma += nota
        contador += 1
    media = soma / contador
    print(f"{nome} tem média {media}")

#9
def mesclar_dicts(d1, d2):
    novo = d1.copy()  
    novo.update(d2)  
    return novo

d1 = {
      "a": 1, 
      "b": 2, 
      "c": 3
}
d2 = {
      "b": 5, 
      "d": 6
}

resultado = mesclar_dicts(d1, d2)
print(resultado)

#10
pontuacoes = {
              "João": 50, 
              "Maria": 80, 
              "Pedro": 70
    }

ordenado = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)

for nome, pontos in ordenado:
    print(f"{nome}: {pontos}")