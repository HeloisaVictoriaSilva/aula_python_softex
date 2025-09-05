# import math
# #1
# def sadaucao():
#     print("Olá, bem-vindo ao Python!")
# sadaucao()
# #2
# def dobro(numero):
#     return numero*2
# print(dobro(int(input("digite um número:"))))

# #3
# def soma(num1, num2):
#     return num1+num2
# print(soma(10,29))

# #4
# def mensagem(nome):
#     if nome:
#         print(f"Olá, {nome}!")
#     else:
#        return print("Olá, visitante!")

# comprimento = input("digite seu nome: ")
# mensagem(comprimento)

# #5
# def operacoes(num1, num2):
#     soma= num1+num2
#     subtracao= num1-num2
#     multiplicacao= num1*num2
#     return soma, subtracao, multiplicacao

# somar, subtrair, multiplicar= (operacoes(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))))
# print(f"soma: {somar} subtração:{subtrair} multiplicação: {multiplicar}")

# #6
# def media(numero1, numero2, numero3):
#     media= (numero1+numero2+numero3)/3
#     return media
# print("a media é: ", media(3, 5, 7))

# #7
# def dados_pessoais(**kwargs):
#     pessoa= {
#         "nome": "Luciana",
#         "idade": 29,
#         "cidade": "Recife"
#     }
#     return pessoa
# print(dados_pessoais())

# #8
# def calculadora(numeros1, numeros2):
#     def soma(numeros1, numeros2):
#         adicao= numeros1+numeros2
#         return adicao
#     def subtracao(numeros1, numeros2):
#         sub= numeros1-numeros2
#         return sub
#     def multiplicar(numeros1, numeros2):
#         multi= numeros1*numeros2
#         return multi
#     def divividir(numeros1, numeros2):
#         divi= numeros1/numeros2
#         return divi
#     while True:
#         opcao = input("Escolha uma opção: \n" \
#                       "1- Somar\n" \
#                       "2- Subtrair\n" \
#                       "3- Multiplicar\n" \
#                       "4- Dividir\n" \
#                       "0- sair\n")
#         match opcao:
#             case "1":
#                 print("Resultado da soma:", soma(numeros1, numeros2))
#             case "2":
#                 print("Resultado da subtração:", subtracao(numeros1, numeros2))
#             case "3":
#                 print("Resultado da multiplicação:", multiplicar(numeros1, numeros2))
#             case "4":
#                 print("Resultado da divisão:", divividir(numeros1, numeros2))
#             case "0":
#                 print("Saindo da calculadora.")
#                 break
#             case _:
#                 print("Opção inválida")

# print(calculadora(int(input("Digite o primeiro número:")), int(input("Digite o segundo número número:"))))

#9
def multiplicar(n1,n2):
    return n1*n2
def adiciona(n1,n2):
   return n1+n2
def aplicar_operacao(n1,n2, operacao):
     return(multiplicar(n1,n2))
     return(adiciona(n1,n2))
print(aplicar_operacao(20,67, adiciona))
print(aplicar_operacao(5,4, multiplicar))