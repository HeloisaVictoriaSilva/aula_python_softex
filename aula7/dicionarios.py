#dicioarios:
#são coleções que receberão valores no formato chave:valor. São ordenados(mas não pode escolher ordem para operações), alteráveis e não permitem valores duplicados.
#permite a duplicação de chaves, mas o último valor atribuído à chave será o que prevalecerá. Aceita valores iguais mas caves iguais não
dicionario = {
    "nome": "João",
    "idade": 25,
    "nacionalidade": "brasileiro"
}
print(dicionario)
#acessando itens:
print(dicionario["nome"])
print(dicionario.get("idade"))#metodo

#listando todos os itens:
print(dicionario.items())

#listando todas as chaves:
print(dicionario.keys())

#listando todos os valores:
print(dicionario.values())

#adicionando itens:
dicionario["altura"] = 1.75
print(dicionario)

#atualizando itens:
#para adicionar item basta colocar uma chave nova
dicionario.update({"idade": 26})

#removendo itens:
dicionario.pop("nacionalidade")
print(dicionario)
dicionario.popitem()#remove o ultimo item adicionado
dicionario.clear()#limpa o dicionario
del dicionario#deleta o dicionario
del dicionario["nome"]#deleta o item especifico

#copiando dicionarios:
dicionario2 = dicionario.copy()
dicionario3 = dict(dicionario)

#iterando por um dicionario:
for itens in dicionario.values():
    if itens == "João":
        print("usuario detectado")


