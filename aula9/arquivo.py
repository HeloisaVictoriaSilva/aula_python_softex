arquivo = open("arquivo.txt", "r")
print(arquivo.read())
arquivo.close()

arquivo = open("arquivo.txt", "a")
arquivo.write("mudando o texto do arquivo")
