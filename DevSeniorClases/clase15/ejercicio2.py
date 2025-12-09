#Sistema de restaurante - POO Avanzada
from abc import ABC,abstractmethod
#list
from typing import List

#SuperClase abstracta persona
class Persona(ABC):
    def __init__(self,nombre:str) ->None:
        self.nombre = nombre
        
    @property
    def nombre(self)-> str:
        return self._nombre
    @nombre.setter
    def nombre(self,nuevo_valor:str)->None:
        if isinstance(nuevo_valor,str) and nuevo_valor.strip():
            self._nombre = nuevo_valor
        else:
            raise ValueError("El nombre debe ser una cadena de texto valida ")
        
    @abstractmethod
    def presentar (self)->None:
        pass
#SubClase
class Cliente (Persona):
    def presentar(self)->None:
        print(f"El cliente {self.nombre} ha llegado al restaurante ")
        
#Interfaz
class Empleado(Persona):
    @abstractmethod
    def trabajar (self)->None:
        pass
class Mesero (Empleado):
    def presentar(self) -> None:
      print(f"El mesero {self.nombre} se encuentra listo para atender")

class Chef(Empleado):
    def presentar(self) ->None:
        print(f"El chef {self.nombre} se encuentra en la cocina")
    def trabajar(self) ->None:
        print(f"El chef { self.nombre} esta preaprando el plato ")
#composicion
class Cocina:
    def __init__(self, chefs:List[Chef])->None:
      self.chefs = chefs
    
    @property
    def chefs(self)->List[Chef]:
        return self._chefs
    @chefs.setter
    def chefs (self,lista_chefs:List[Chef]) ->None:
        if isinstance (lista_chefs,List)and all (isinstance(c,Chef) for c in lista_chefs):
            self._chefs = lista_chefs
        else:
            raise ValueError("Debe proporcionar una lista valida de objetos de tipo chef.")
    def operar(self)-> None:
       for chef in  self.chefs:
           chef.trabajar()
#Agregacion/composicion
class Restaurante:
    def __init__(self,nombre:str)->None:
        self.nombre = nombre
        self.clientes: List[Cliente] = []
        self.cocina = Cocina ([Chef("Lusi"),Chef("Daniel")])#Composicion muy fuerte
    @property
    def nombre(self) -> str:
        return self._nombre 
    
    @nombre.setter
    def nombre (self,nuevo_nombre:str) ->None:
        if isinstance(nuevo_nombre,str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre del restaurante debe ser un nombre valido ")
    
    def agregar_cliente (self,cliente:Cliente) -> None:
        if isinstance(cliente,Cliente):
            self.clientes.append(cliente)
        else:
            raise ValueError("Solo se pueden agregar elementos de tipo cliente.")
    def iniciar_servicio(self)->None:
        print(f"\n*** El restaurante {self.nombre} iniciando el servicio ***")
        print("\n Atendiendo a los siguientes clientes:")
        
        for cliente in  self.clientes:
            cliente.presentar()
        
        print("\nCocina en operacion ")
        self.cocina.operar()
def main() -> None:
    restaurante = Restaurante("El buen gusto")
    
    restaurante.agregar_cliente(Cliente("Santiago Romero"))
    restaurante.agregar_cliente(Cliente("Juan Rodriguez"))
    
    restaurante.iniciar_servicio()

if __name__ == "__main__":
    main()
        
           
        
    
        
        
