import math
#1
def sadaucao():
    print("Olá, bem-vindo ao Python!")
sadaucao()
#2
def dobro(numero):
    return numero*2
print(dobro(int(input("digite um número:"))))

#3
def soma(num1, num2):
    return num1+num2
print(soma(10,29))

#4
def mensagem(nome):
    if nome:
        print(f"Olá, {nome}!")
    else:
       return print("Olá, visitante!")

comprimento = input("digite seu nome: ")
mensagem(comprimento)

#5
def operacoes(num1, num2):
    soma= num1+num2
    subtracao= num1-num2
    multiplicacao= num1*num2
    return soma, subtracao, multiplicacao

somar, subtrair, multiplicar= (operacoes(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))))
print(f"soma: {somar} subtração:{subtrair} multiplicação: {multiplicar}")

#6
def media(numero1, numero2, numero3):
    media= (numero1+numero2+numero3)/3
    return media
print("a media é: ", media(3, 5, 7))

#7
def dados_pessoais(**kwargs):
    pessoa= {
        "nome": "Luciana",
        "idade": 29,
        "cidade": "Recife"
    }
    return pessoa
print(dados_pessoais())

#8
def calculadora():
    def soma(numeros1, numeros2):
        adicao= numeros1+numeros2
        return adicao
    def subtracao(numeros1, numeros2):
        sub= numeros1-numeros2
        return sub
    def multiplicar(numeros1, numeros2):
        multi= numeros1*numeros2
        return multi
    def divividir(numeros1, numeros2):
        divi= numeros1/numeros2
        return divi
    # numero = input("Escolha uma opção: \n " \
    #               "1- Somar\n "\
    #                 "2- Subtarir\n" \
    #                 "3- Multiplicar\n" \
    #                 "4- Dividir\n"\
    #                 "0- sair")
    # match numero:
    #     case "1":
            
    #         break
    #     case _:
    #         print("opção invalida")

