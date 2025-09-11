# #1
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"Nome do aluno: {self.nome}, Idade: {self.idade}"
    #2
    def apresentar(self):
        print(f"olá, meu nome é João e tenho 20 anos")
aluno1= Pessoa("Girleite", 18)
aluno2= Pessoa("Rivineido", 32)
aluno1.apresentar()
print(aluno1)
print(aluno2)
# print(f"Nome do aluno 1: {aluno1.nome}, Idade: {aluno1.idade}")
# print(f"Nome do aluno 2: {aluno2.nome}, Idade: {aluno2.idade}")

# #3
class Carro:
    def __init__(self,marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"
carro1 = Carro("Renault", "Kwid", 2020)
carro2 = Carro("Fiat", "Mobi", 2021)
carro3 = Carro("Chevrolet", "Onix", 2022)
print(carro1)
print(carro2)
print(carro3)
#4
carro_ano= Carro("Ford", "Ka", 2019)
print(carro_ano)
carro_ano.ano= 2024
print(carro_ano)

# #5 e 6
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular= titular
        self.saldo= saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"Saldo alterado: {self.saldo}")
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque realizado com sucesso, novo saldo: {self.saldo}")
            return print(True)
        else:
            print("saldo insuficiente para saque")
            return print(False)
conta_bancaria1 = ContaBancaria(input("Digite o nome do titular da conta: "), float(input("Digite o saldo inicial da conta: ")))
conta_bancaria1.depositar(float(input("Digite o valor a ser depositado: ")))
conta_bancaria1.sacar(float(input("Digite o valor a ser sacado: ")))

#7 e 8
class Aluno:
    def __init__(self,nome,nota):
        self.nome= nome
        self.nota=nota
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.aluno= []
    def adicionar_aluno(self,alunos):
        self.aluno.append(alunos)
        print(f"Aluno adicionado a lista")

estudante1= Aluno("Aurora", 9.5)
estudante2= Aluno("Jasmine", 7.8)
estudante3= Aluno("Alan", 6.5)
estudante4= Aluno("Joaquim", 8.7)
turma1= Turma()
turma1.adicionar_aluno(estudante1)
turma1.adicionar_aluno(estudante2)
turma1.adicionar_aluno(estudante3)
turma1.adicionar_aluno(estudante4)
print("lista atual com todos os alunos: ",[str(a) for a in turma1.aluno])

#9
class Cachorro:
    especie= "Canis familiaris"
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade
    def __str__(self):
        return(f"nome: {self.nome}, idade: {self.idade}")

cachorro1 = Cachorro("Belinha", 4)
print(cachorro1, "especie: ",cachorro1.especie)
cachorro2 = Cachorro("Big", 6)
cachorro2.especie = "chihuahua"
print(cachorro2, "especie: ",cachorro2.especie)
 