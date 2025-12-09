#monster inc
# from abc import ABC, abstractmethod
# class Mounstro():
#     pass
#En python la clase es ese molde de cortar galletas para que todos los elementos sean iguales 
from abc import ABC, abstractmethod
class Mounstro(ABC):
# el constructor le da vida a la clase 
    def __init__(self, nombre , color , poder):
        self.nombre = nombre
        self.color = color 
        self.poder = poder
    def asustar (self,Mountro):
        return f"{self.nombre} esta asutando con su poder {self.poder}"
        
        
#Los objetos
   #Crear objetos se llama instanciar apartir de una clase     
marian=Mounstro("Marian","Azul","Pregunta")
santiago=Mounstro("Santiago","rojo" ,"callado")
#Metodos son las acciones que puedne hacer los objetos



print(marian.asustar)



