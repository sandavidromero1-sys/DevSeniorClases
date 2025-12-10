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
#Metodos son las acciones que puedne hacer los objetos
    def asustar (self):
        return f"{self.nombre} esta asutando con su poder {self.poder}"
class MounstroPreguntador(Mounstro):
    def preguntar(self):
        return f"{self.nombre} esta preguntando todo el tiempo"
class MounstroDormilon(Mounstro):
    def __init__(self, nombre , color, poder):
       super().__init__(nombre, color , poder)
    def dormir(self):
        return f"{self.nombre} se esta durmiendo en el turtorial "

        
        
#Los objetos
   #Crear objetos se llama instanciar apartir de una clase     
marian=MounstroPreguntador("Marian","Azul","Pregunta")
santiago=MounstroDormilon("Santiago","gris", "ronquido supremo")
juan=Mounstro("juan","azul" ,"amargado")




print(marian.asustar())
print(marian.preguntar())
print(juan.asustar())

#herencia son las cualidades que podemos utilizar del padres 

#super clase es la clase padre de la cual se puede heredar cualidades y metodos 
#sub clase es ña clase hija que hereda de cualidades y metodos de la super clase 




