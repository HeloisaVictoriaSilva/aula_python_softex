#1
from abc import ABC, abstractmethod
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass
    
class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento no cartão de credito no valor de: {valor} "
    

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Processando pagamneto ddo Boleto no valor de: {valor}"


pagamento = CartaoCredito()
print(pagamento.processar(valor= 765))
pagamento1= Boleto()
print(pagamento1.processar(valor=32))

#2
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel):
    def ligar(self):
        return f"O computador esta ligado"
    def desligar(self):
        return f"O computador esta desligado"
    
notebook= Computador()
print(notebook.ligar())
print(notebook.desligar())

#3
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return f"Imprimindo relatorio"
    def exportar(self):
        return f"Exportando relatorio"
    
relatorio= Relatorio()
print(relatorio.imprimir())
print(relatorio.exportar())

#4
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    @abstractmethod
    def buscar(self, id):
        pass

class  RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return f"repositorio salvo, objeto: {objeto}"
    
repositorio= RepositorioMemoria()
print(repositorio.salvar(objeto=987))

# A classe RepositorioMemoria herda uma classe e metodos abstrados então 
# como não foi implementado todos os métodos abstrados, 
# enquanto todos os métodos abstratos não forem instanciados 
# a classe não pode ser implementada corretamente

