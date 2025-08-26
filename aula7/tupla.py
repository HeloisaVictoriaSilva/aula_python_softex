#tupla: é uma coleção que pode conter vários tipos de dados e é imutavel, não pode ser alterada depois de sua criação
#sintaxe: tupla = (valor1, valor2, valor3)
#tuplas  com único elemento precisa terminar com uma vírgula, caso contrario o pythopn não entende que é uma tupla e sim uma string
tupla =("lua", 34, [1,2,3,4])
tupla1 = ("sol",)
tupla2 = 1,2,
print(type(tupla))

#metodos de tuplas
print(tupla.count(34)) # conta quantas vezes o valor aparece na tupla
print(tupla.index("lua")) # retorna o indice do valor na tupla


