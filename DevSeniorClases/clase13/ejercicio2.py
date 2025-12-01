class Empleado:
    def __init__(self,nombre:str):
        if not Empleado.validar_nombre(nombre):
            raise ValueError("El nombre debe ser un texto valido")
        
        self.nombre = nombre
    
    def trabajar(self) -> None:
        print(f"{self.nombre} esta realizando tareas generales")
    
    @staticmethod  
    def validar_nombre(nombre:str)-> bool:
        return isinstance(nombre,str) and nombre.strip() != ""
    
class Gerente(Empleado):
    def trabajar(self)-> None:
        print(f"{self.nombre} esta coordinando los proyectos a su cargo")
    def comision(self):
        pass
    
class Desarrolador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta codificando un backend en python")

def ejecutar_tarea(empleado:Empleado)-> None:
    empleado.trabajar()
    
def main() -> None:
    print("\n¿Es valido introducir Gilberto?", Empleado.validar_nombre("Gilberto"))
    print("\n¿Es valido este nombre?", Empleado.validar_nombre(""))
    print("\n¿Es valido este nombre 55555?", Empleado.validar_nombre("55555"))
    print("\n¿Es valido 22222?\n", Empleado.validar_nombre("22222"))
    
    empleado1 = Gerente("MARYAM")
    empleado2 = Desarrolador("Juan")
    
    ejecutar_tarea(empleado1)
    ejecutar_tarea(empleado2)

if __name__ == "__main__":
     main()
