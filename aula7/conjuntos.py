#conjuntos: outro tipo de dado capaz de armazenar vários valores,. Os conjntos não são ordenados nem idexados
# e não aceita repetição de dados. usa chaves {}
conjunto = {"duna", "fundação", "neuromancer"}
#acessando itens de um conjunto:
# usando o for ou in
print("duna" in conjunto)

#mudando itens de um conjunto

#adicionando itens:
conjunto.add("o conto da aia")
conjunto.update(["1984", "laranja mecânica"])# adiciona qualquer iteravel ao conjunto

#removendo itnes
conjunto.remove("duna") #retorna o erro
conjunto.discard("fundação") #não retorna o erro
conjunto.pop() #remove um item aleatório
conjunto.clear() #limpa o conjunto
del conjunto #deleta o conjunto, ferramenta de limpeza de memória do python

#outros metodos do conjunto
conjunto.union() # une dois conjuntos
#conjunto|# une dois conjuntos
conjunto.intersection() # retorna a interseção entre dois conjuntos
#conjunto & # retorna a interseção entre dois conjuntos
conjunto.difference() # retorna a diferença entre dois conjuntos
#conjunto - # retorna a diferença entre dois conjuntos
conjunto.symmetric_difference() # retorna a diferença simétrica entre dois conjuntos
#conjunto ^ # retorna a diferença simétrica entre dois conjuntos