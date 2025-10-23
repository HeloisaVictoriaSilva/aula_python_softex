#1
class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo
    def descricao_livro(self):
        print(f"Título do livro: {self.titulo}")

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def ler_livro(self, livro: Livro):
        print(f"A pessoa {self.nome} esta lendo {livro.titulo}")

livro1= Livro("Percy jackson e a batalha no labirinto")
pessoa1= Pessoa("Alice")
pessoa1.ler_livro(livro1)

#2
class Onibus:
    def __init__(self, linha: str):
        self.linha = linha
    
class Aluno:
    def __init__(self, nome: str):
        self.nome= nome
    def pegar_onibus(self, onibus: Onibus):
        print(f"O aluno esta no onibus: {onibus.linha}")

onibus1= Onibus(linha= "TI Trancredo Neves/ Conde da boa vista")
aluno1= Aluno(nome= "Talia")
aluno1.pegar_onibus(onibus1)

#3
class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome

class Departamento:
    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []
    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"O funcionario (a): {funcionario.nome} esta incerido no {self.nome}")

funcionario1 = Funcionario("Solange")
funcionario2 = Funcionario("Paulo")
funcionario3 = Funcionario("Carmem")
funcionario4 = Funcionario("Gustavo")

departamento1 = Departamento("RH")
departamento1.adicionar_funcionario(funcionario1)
departamento1.adicionar_funcionario(funcionario2)
departamento1.adicionar_funcionario(funcionario3)
departamento1.adicionar_funcionario(funcionario4)

departamento1.listar_funcionarios()

#4
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao= posicao

class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time
        self.jogadores = []

    def adicionar_jogadores(self, jogador: Jogador):
        self.jogadores.append(jogador)
    def listar_jogador(self):
        for jogador in self.jogadores:
            print(f"O jogador {jogador.nome} está na posição {jogador.posicao}")

jogador1 = Jogador("Gabriel", "Goleiro")
jogador2 = Jogador("Enzo", "Defesa")
jogador3 = Jogador("Luiz", "Meio campo")
jogador4 = Jogador("Antonio", "Atacante")

time1 = Time("Ibis")
time1.adicionar_jogadores(jogador1)
time1.adicionar_jogadores(jogador2)
time1.adicionar_jogadores(jogador3)
time1.adicionar_jogadores(jogador4)

time1.listar_jogador()

#5
class Motor:
    def __init__(self, potencia: int):
        self.potencia = potencia
    def ligar(self):
        print(f"O motor está ligado, potencia: {self.potencia}")
    def __del__(self):
        print("O motor foi destruido")

class Carro:
    def __init__(self, marcar: str, potencia_motor: int):
        self.marcar = marcar
        self.motor = Motor(potencia_motor)
    def desligar_carro(self):
        print(f"Ligando o carro da marcar: {self.marcar}")
        self.motor.ligar()
    def __del__(self):
        print("O carro foi destruido")

carro1= Carro("Kwid", 71)
carro1.desligar_carro()

del carro1

#6
class Cozinha:
    def __init__(self, fogao_modelo):
        self.fogao_modelo= fogao_modelo
    def __str__(self):
        return f"O modelo do fogão da cozinha é: {self.fogao_modelo}"

class Banheiro:
    def __init__(self, disponivel):
        self.disponivel= disponivel
    def __str__(self):
        return f"O banheiro está disponivel"
class Casa:
    def __init__(self, endereco_casa, fogao_modelo1, banheiro_disponivel):
        self.endereco_casa = endereco_casa
        self.cozinha= Cozinha(fogao_modelo1)
        self.banheiro= Banheiro(banheiro_disponivel)
    def criar_casa(self):
        print(f"Criando casa com fogão: {self.cozinha}, com banheiro: {self.banheiro}")

casa1 = Casa("Rua da guia", "Bramtemp", "disponivel")

print(casa1.criar_casa())