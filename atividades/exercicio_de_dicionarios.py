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
