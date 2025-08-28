#funções: evita repetição de codigo
#uma função é um bloco de código que só é executado quando é chamado
#é obrigatório o uso de parênteses para chamar a função
# def nome_funcao():
#     print("função executada")
# nome_funcao()

def ola(msg, numero):
    print(msg + numero)

ola("ola mundo", "68")

#return
#é usado para retornar um valor de uma função
def soma(num1, num2):
    global valor_somado 
    valor_somado = num1 + num2
    if valor_somado > 1:
        return "maior que 1"
    if valor_somado <= 1:
        return "menor que 1"
    return valor_somado
valor = soma(2,3)
print(valor_somado)
print(f"A soma retornou: {valor}")


