#1
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
    def descricao_livro(self):
        print(f"Título do livro: {self.titulo}")

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def ler_livro(self, livro):
        print(f"O livro {livro.titulo} esta sendo lido por {self.nome}")

livro1= Livro("Percy jackson")
pessoa1= Pessoa("Alice")

print(pessoa1.ler_livro(livro1))

#2
class Onibus:
    def __init__(self, linha):
        self.linha = linha
    
class Aluno:
    def __init__(self, nome):
        self.nome= nome
    def pegar_onibus(self, linha):
        print(f"O aluno esta no onibus: {Onibus.linha}")

onibus1= Onibus(linha= "TI Trancredo Neves/ Conde da boa vista")
aluno1= Aluno(nome= "Talia")
print(aluno1.pegar_onibus((onibus1)))
