from abc import ABC,abstractmethod

class Animal(ABC):
    
    def __init__(self, nombre):
        self.nombre = nombre
    @abstractmethod
    def hacerSonido(self)->None:
        pass
class Movible(ABC):
  @abstractmethod
  def mover(self)->None:
   pass

class Perro (Animal):
    def hacerSonido(self)->None:
       print(f"{self.nombre} ladrando")
class Gato (Animal):
    def hacerSonido(self)->None:
       print(f"{self.nombre} Maullando")
class Vaca (Animal):
    def hacerSonido(self)->None:
       print(f"{self.nombre} Mujiendo ")
class Leon(Animal,Movible):
    def hacerSonido(self)->None:
       print(f"{self.nombre} Mujiendo ")
    def mover(self):
       print(f"El leon {self.nombre} se esta moviendo por la sabana Africana")

def RealizarSonido(animal:Animal) -> None:
    animal.hacerSonido()
    
def main() -> None:
    perro = Perro("Bruno")
    gato = Gato("Messi")
    vaca = Vaca("Lola")
    leon = Leon("Simba")

    print("\nSonidos de Animales\n")
    
    RealizarSonido(perro)
    RealizarSonido(gato)
    RealizarSonido(vaca)
    RealizarSonido(leon)
    
    print("\nMovimientos\n")
    
    leon.mover()
if __name__ == "__main__":
    main()
    
    

        