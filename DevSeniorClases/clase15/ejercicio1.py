from abc import ABC,abstractmethod
from typing import Optional #TIPADO FUERTE => tying: List, Tuble, Dict

#Interfaz movible
class Movible (ABC):
    @abstractmethod
    def mover(self)-> None:
        pass
#superclase abstracta
class Animal (ABC):
    def __init__(self, nombre:str) -> None:
       self._nombre:str = ""
       self.nombre = nombre
    @property
    def nombre (self)-> str:
        return self._nombre
    @nombre.setter
    def nombre(self,valor:str)->None:
        if isinstance(valor,str) and valor.strip():
            self._nombre = valor.strip().title()
        else:
            raise ValueError("Error al ingresar el nombre, ingre un nombre valido")
    @abstractmethod
    def sonido (self)-> None:
        pass
    
#subclases

class Perro(Animal):
    def sonido(self) ->None:
        print(f"El perro {self.nombre} dice: guau guau  ")
class Gato(Animal):
    def sonido(self) ->None:
        print(f"El gato {self.nombre} dice: miau miau")
class Vaca(Animal):
    def sonido(self) ->None:
        print(f"La vaca {self.nombre} dice: MUUUUUU  ")
class Leon(Animal,Movible):
    def sonido(self) ->None:
        print(f"El leon{self.nombre} dice: GRRRRRRRRR ")
    def mover(self):
        print(f"El leon {self.nombre} Camina por la sabana......")
        
        
        
        
    