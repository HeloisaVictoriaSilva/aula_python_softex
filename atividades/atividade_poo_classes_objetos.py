#1
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

#3
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

#5
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
        else:
            print("saldo insuficiente para saque")

#6