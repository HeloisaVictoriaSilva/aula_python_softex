#1
try:
    numero= int(input(("Digite um número: ")))
    print(f"Você digitou {numero}")
except ValueError:
     print("Você digitou um dado errado, digite um número inteiro")
# except Exception as erro:
#     print(f"tivemos um erro de {erro.__class__}")

#2
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo numero: "))
    multiplicação = numero1/numero2
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados digitados")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados") 
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado da multiplicação é: {multiplicação}")

#3
try:
    numero_inteiro= int(input("Digite um número inteiro: "))
except (ValueError, TypeError):
    print("Os dados digitados não são um número inteiro")
except KeyboardInterrupt:
    print(" O usuário preferiu não digitar os dados solicitados")
except Exception as erro:
    print(f"Um erro foi encontrado {erro.__cause__}")
else:
    print("O dado digitado foi um número inteiro e a conversão ocorreu corretamente")

#4
try:
    open("dados.txt", "r")
except FileNotFoundError:
    print("arquivo não existe")
finally:
    print("Encerrando programa")

#5
def dividir(a,b):
    if b==0:
        raise ZeroDivisionError("O denominador não pode ser zero")
    elif b!=0:
        divisão= a/b
        print(divisão)
    #else:
       # print(divisão)
    
dividir(int(input("Digite um número para o numerador: ")), int(input("Digite um número para o denominador: ")))

#6
class IdadeInvalidaError(Exception):...

try:
    idade = int(input("Informe a idade: "))
    if idade <= 0:
        raise IdadeInvalidaError("idade não pode ser negativa ou zero")
except IdadeInvalidaError as erro:
    print(type(erro).__name__,":", erro)


def cadastrar_idade(idade):
    if idade <= 0:
      raise IdadeInvalidaError("A idade é negativa ou zero, digite uma idade valida")

#7
try:
    numerador= int(input("Digite um numerador: "))
    denominador= int(input("Digite o denominador: "))
    dividir= numerador/denominador
    print(f"O resultado da divisão: {dividir}")
except ValueError :
    print("número invalido, digite um número valido")
except ZeroDivisionError:
    print("denominador não pode ser zero, digite outro número")

#8
try:
    numero_inteiro= int(input("Digite um numero inteiro: "))
    if numero_inteiro % 2 == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é ímpar")
except (ValueError, TypeError):
    print("O usuario não digitou um número inteiro")
except KeyboardInterrupt:
    print("O usuario preferiu não digitar o número")
finally:
    print("Fim do programa")

#9
class SaldoInsuficienteError (Exception):...
try:
    saldo = int(input("Informe o saldo da conta: "))
    valor = int(input("Digite o valor a ser sacado: "))
    if saldo < valor:
        raise SaldoInsuficienteError ("Erro: o valor a ser sacado é maior que o saldo na conta")
except SaldoInsuficienteError  as erro:
    print(type(erro).__name__,":", erro)

def sacar(saldo, valor):
    if saldo<valor:
        raise SaldoInsuficienteError("Erro: o valor a ser sacado é maior que o saldo na conta")
    elif saldo>valor:
        saldo_atual= saldo - valor
        print(f"Saque realizado com sucesso, novo saldo: R$: {saldo_atual}")
        return saldo_atual
sacar(saldo, valor)
