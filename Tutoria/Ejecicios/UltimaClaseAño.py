from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def hacer_sonido():
       pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Wof"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Mew"