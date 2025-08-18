#condicionais
#if = se
 #   else = então
#elif = se não, se| se as condições anteriores não forem verdadeiras, então tente esta condição
#Menor de isdade> paga meia, adulto não tem promoção, idoso tem gratuidade
# Operadores lógicos:
#and = e, todas as condições precisam ser verdadeiras
#or = ou, basta uma ser verdadeira
#not = não, inverte o valor lógico (true -> false, false -> true)
#strip() = remove espaços extras/brancos(ex.: " sim " -> "sim")
#lower() = coloca tudo em minusculo (ex.: "SIM" -> "sim")
#pass = não faça nada aqui,

idade_cliente = int(input("informe a idade do cliente: "))
resposta_dia = input("È quarta feira? (S/N):")

#transformando resposta em boolean
dia_quarta = (resposta_dia == "S")


if idade_cliente >= 60:
    print("cortesia 100%")
elif dia_quarta: 
   print("cortesia 50%")
elif idade_cliente <= 18:
    print("cortesia 10%")
else:
    print("cliente sem cortesia")