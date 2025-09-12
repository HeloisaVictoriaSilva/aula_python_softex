#1
# try:
#     numero= int(input(("Digite um número: ")))
#     print(f"Você digitou {numero}")
# except ValueError:
#      print("Você digitou um dado errado, digite um número inteiro")
# # except Exception as erro:
# #     print(f"tivemos um erro de {erro.__class__}")

#2
# try:
#     numero1 = float(input("Digite o primeiro número: "))
#     numero2 = float(input("Digite o segundo numero: "))
#     multiplicação = numero1/numero2
# except (ValueError, TypeError):
#     print("Tivemos um problema com os tipos de dados digitados")
# except KeyboardInterrupt:
#     print("O usuário preferiu não informar os dados") 
# except Exception as erro:
#     print(f"O erro encontrado foi {erro.__cause__}")
# else:
#     print(f"O resultado da multiplicação é: {multiplicação}")

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
