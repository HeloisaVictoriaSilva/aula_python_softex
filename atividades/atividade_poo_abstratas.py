from abc import ABC, abstractmethod
#1
# class Animal (ABC):
#     @abstractmethod
#     def falar():
#         pass

# class Cachorro(Animal):
#     def falar(self):
#         print("AU AU")
    
# class Gato(Animal):
#     def falar(self):
#         print("miau miau")
    
# belhinha= Cachorro()
# print(belhinha.falar())

# mel= Gato()
# print(mel.falar())

#2
# class Animal (ABC):
#      @abstractmethod
#      def falar():
#          print("AU AU")

# cachorro= Animal()
# print(cachorro.falar)
# #A classe abstrata não pode ser implementada, precisa de uma outra classe concreta para isso

#3
class FormaGeometrica(ABC):
     @abstractmethod
     def area(self):
          pass
     @abstractmethod
     def perimetro(self):
          pass
     
class Retangulo(FormaGeometrica):
     def area(self, x, y):
          area_retanulo= x * y
          return area_retanulo
     def perimetro(self,x,y):
          perimetro_retangulo= 2 * (x + y)
          return perimetro_retangulo
     
retangulo= Retangulo()
print(retangulo.area(5,3))

print(retangulo.perimetro(5,3))

#4
class Trasnporte(ABC):
     @abstractmethod
     def mover():
          pass
     @abstractmethod
     def parar():
          pass

class Carro(Trasnporte):
     def mover(self):
          return "Correndo"
     
kiwid= Carro()
print(kiwid.mover())

# A classe carro herda uma classe e metodos abstrados então 
# como não foi implementadon todos od métodod abstratos, 
# enquanto todos os métodos abstratos não forem instanciados 
# a classe não pode ser implementada

#codigo corrigida:
class Trasnporte(ABC):
     @abstractmethod
     def mover():
          pass
     @abstractmethod
     def parar():
          pass

class Carro(Trasnporte):
     def mover(self):
          return "Correndo"
     def parar(self):
          return "Parado"
     
kiwid= Carro()
print(kiwid.mover())
print(kiwid.parar())