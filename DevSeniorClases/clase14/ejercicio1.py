from abc import ABC,abstractmethod

class Empleado(ABC):
    def __init__(self, nombre:str)->None:
        self._nombre = None
        self.nombre = nombre
        
        @property
        def nombre(self) -> str:
            return self._nombre
        
        @nombre.setter
        def nombre(self, valor:str)->None:
            if isinstance(valor,str) and valor.strip():
                self._nombre = valor.strip()       
            else:
                raise ValueError("El nombre debe ser un texto no vacio")
        @abstractmethod
        def trabajar(self)->None:
            pass
        
class Gerente (Empleado):
    def trabajar(self)->None:
        print(f"{self.nombre} esta gestionando estrategias empresariales ")
        
class Desarrollador (Empleado):
    def trabajar(self)->None:
        print(f"{self.nombre} esta desarrollando software")
def ejecutar_tarea(empleado:Empleado) -> None :
   empleado.trabajar()
def main() ->None:
    empleado1= Gerente("Santiago")
    empleado2 = Desarrollador("David")
    
    ejecutar_tarea(empleado1)
    ejecutar_tarea(empleado2)
    
    empleado2.nombre = "Juan"
    print(f"El nombre nuevo es: {empleado2.nombre} ")
    empleado1.nombre = "Pedro"
    print(f"El nombre nuevo es: {empleado1.nombre} ")
    
    ejecutar_tarea(empleado1)
    ejecutar_tarea(empleado2)
    
if __name__ == "__main__":
    main()
    
 