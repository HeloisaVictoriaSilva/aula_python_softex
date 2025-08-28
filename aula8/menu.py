# num = input("digite um número de 1 a 5:")
# match num:
#     case "1":
#         print("você digitou 1")
#     case "2":
#         print("você digitou 2")
#     case "3":
#         print("você digitou 3")
#     case "4":
#         print("você digitou 4")
#     case "5":
#         print("você digitou 5")
#     case_:
#         print("número invalido")

#combinar valores

#Criando menu com match

def adicionando_livros():
    global casa
    casa = 3
    print("adicionando livros")
    
while True:
    opcao = input("Escolha uma opção: \n " \
                  "1- criar entrada\n "\
                    "2- editar informações de um livro cadastrado\n" \
                    "3- apagar um livro cadastrado\n" \
                    "4- deletar um livro\n"\
                    "0- sair")
    match opcao:
        case "1":
            adicionando_livros()
            print(casa)
        case "2":
            print("editando livros")
        case "3":
            print("pesquisando livros")
        case "4":
            print("deletando livro")
        case "0":
            break
        case _:
            print("opção invalida")
            
