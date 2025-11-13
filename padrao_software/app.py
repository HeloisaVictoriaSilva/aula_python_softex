from abc import ABC, abstractmethod

#interface das classes concretras
class Midia(ABC):
    def ler_midia(): ...

class ebook(Midia):
    def __init__(self, tipo, nome):
        self.tipo= tipo
        self.nome = nome
    def ler_midia(self) -> str:
        print(f"Lendo o ebook: {self.nome}")

class Audio(Midia):
    def __init__(self, tipo, nome):
        self.tipo= tipo
        self.nome = nome

    def ler_midia(self) -> str:
        print(f"Ouvindo musica: {self.nome}")

musica1= Audio("classica", "memoria")
musica1.ler_midia()

#criando as fabricas
class fabric_midia(ABC):
    @abstractmethod
    def fabric_method(self, midia:Midia):
        midia.ler_midia()

class fabric_ebook(fabric_midia):
    def fabric_method(self):
        ebook.ler_midia()

fabric_ebook()