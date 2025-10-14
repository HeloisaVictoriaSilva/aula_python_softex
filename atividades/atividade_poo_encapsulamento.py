#1
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular= titular
        self.__saldo= saldo
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo= novo_saldo
        else:
            print("Saldo negativo ou zerado!")
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f"Saldo alterado: {self.saldo}")
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Saque realizado com sucesso, novo saldo: {self.saldo}")
            return print(True)
        else:
            print("saldo insuficiente para saque")
            return print(False)
conta_bancaria1 = ContaBancaria(input("Digite o nome do titular da conta: "), float(input("Digite o saldo inicial da conta: ")))
conta_bancaria1.depositar(float(input("Digite o valor a ser depositado: ")))
conta_bancaria1.sacar(float(input("Digite o valor a ser sacado: ")))

#2
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade
    def __str__(self):
        return f"Dados do usuário -> nome: {self.nome}, data de nacimento: {self.data_nascimento}, CPF: {self.cpf}, identidade: {self.identidade}"
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf_N):
        if len(cpf_N) == 11:
            self.__cpf = cpf_N
        else:
            return "CPF inválido, digite a quantidade de números correta"
    @property
    def identidade(self):
        return self.__identidade
    @identidade.setter
    def identidade(self, identidade_N):
         self.__identidade = identidade_N

pessoa1 = Pessoa("Heloisa", "06/04/20005", 65433, 86544)
print(pessoa1)
