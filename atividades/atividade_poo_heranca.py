#1, 2, 3, 4
class Usuario:
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email
    def exibir_informacoes(self):
        return f"Nome do úsuario: {self.nome}, email: {self.email}"
    def saudacao(self):
        print(f"Olá usuario {self.nome}")
class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo
    def exibir_informacoes(self):
        return super().exibir_informacoes()
    def saudacao(self):
        return f"Olá Cliente {self.nome}"
    # def __str__(self):
    #     return f"Nome do úsuario: {self.nome}, email: {self.email}"

#5, 6, 7
class Funcionario(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

class Gerente(Funcionario):
    def __init__(self, nome, email):
        super().__init__(nome, email) 

cliente1 = Cliente("Heloisa", "heloisa@gmail.com", 654)
usuario1 = Usuario("Ana", "ana@gmail.com")
gerente1 = Gerente("Carolina", "carolina@gmail.com")
print(usuario1.exibir_informacoes())
print(cliente1.exibir_informacoes())
print(cliente1.saudacao())
print(usuario1.saudacao())
print(gerente1.exibir_informacoes())

#6
class  Autenticacao:
    def login(self, email, senha):
        if email and senha:
            print("Login efetuado com sucesso!")
        else:
            return "Login não efetuado, digite as informações corretamente"
    def status(self):
        return "status da Autenticação"

class Permissao:
    def verificar_permissao(self, usuario):
        return f"Verificando permissões do usuário {usuario}"
    def status(self):
        return "status da Permissão"

class Administrador(Autenticacao, Permissao):
    pass

admin = Administrador()
print(admin.login(input("Digite a seu email: "), input("Digite a sua senha: ")))
print(admin.verificar_permissao("Heloisa"))
print(Autenticacao.status(admin))
print(Permissao.status(admin))
