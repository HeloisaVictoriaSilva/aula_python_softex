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
class Animal (ABC):
     @abstractmethod
     def falar():
         print("AU AU")

cachorro= Animal()
print(cachorro.falar)
#A classe abstrata não pode ser implementada, precisa de uma outra classe concreta para isso

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
          return super().area()
     