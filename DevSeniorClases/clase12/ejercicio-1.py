"""
class Vehiculo:
    def mover(self):
        print("El vehiculo se esta moviendo")
        
class Carro(Vehiculo):
    pass
def main():
    vehiculo1 = Vehiculo()
    carro1 = Carro()
    
    print("Vehiculo")
    vehiculo1.mover()
    print("Carro que hereda de la super clase Vehiculo")
    carro1.mover()
    
    if __name__ == "__main__":
        main()
"""
"""
#Sobre escritur 
#Herencia
class Vehiculo ():
    def  mover(self):
        print("El vehiculo se esta moviendo ")
        
class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle ")
        
def main():
    vehiculo2 = Vehiculo()
    carro2 = Carro()
    
    print("Vehiculo")
    vehiculo2.mover()
    
    print("El carro sobre escribio el metodo (def) mover ya que su movimiento  es atraves de ruedas")
    carro2.mover()
    
if __name__ == "__main__":
        main()
"""
"""
#Polimorfismo
class Vehiculo ():
    def mover(self):
        print("El vehiculo se esta moviendo")
        
class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle ")

class Avion(Vehiculo):
    def mover(self):
        print("El avion vuela sobre la ciudad ")
        
def main():
    vehiculo3 = Vehiculo()
    carro3 = Carro()
    avion3 = Avion()
    
    print("Vehiculo")
    vehiculo3.mover()
    
    print("Carro")
    carro3.mover()
    
    print("Avion")
    avion3.mover()
    
if __name__ == "__main__":
    main()
"""
"""
#super()
class Padre():
 def __init__(self,mensaje)-> None:
    self.mensaje = mensaje 
    
class Hijo (Padre):
 def __init__(self, mensaje, nombre)-> None :
    super().__init__(mensaje)
    self.nombre = nombre 
    
def main():
    objeto1 = Hijo("Hola desde la clase hijo " , "Por ende necesita dos arguentos ")
    print(objeto1.mensaje)
    print(objeto1.nombre)
    
if __name__  == "__main__":
    main()
"""
"""
class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario,departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Salario: {self.departamento}")
        
def main():
    gerente = Gerente ("Luis molero",343243433432,"Tic")
    gerente.mostrar_informacion()
    
if __name__ == "__main__":
    main()
"""
"""
#Ejemplo con polimorfismo
class Empleado():
    def __init__(self, nombre:str)-> None:
        self.nombre = nombre
        
    def trabajar(self):
        print(f"{self.nombre} esta realizando una tarea general")
        
class Gerente(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta desarrolando software")

class Desarrollador (Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta desarrollando software")
        
def main():
    empleados = [
        Gerente("SANTIAGO"),
        Desarrollador("Juan Esteban"),
        Empleado("Kevin")
    ]
    
    print("Polimorfismo")
    for empleado in empleados:
        empleado.trabajar()
        
if __name__ == "__main__":
    main()
    
"""  
#POLIMORFISMO CON FUNCIONES QUE RECIBEN CUALQUIER OBJETO 
# deasarrolle una  super aplicacion para una Veterinaria
# Superclase:
## Animal
#subclase:
# perritos
# gaticos 

class Animal():
     def __init__(self,nombre):
         self.nombre = nombre 

class Perro (Animal):
    def __init__(self, nombre,raza):
       super().__init__(nombre)
       self.raza = raza

class Gato (Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

def main():
    perro = Perro("Bruno","Golden")
    gato = Gato("Messi",3)
    
    print(f"el nombre del perro es {perro.nombre} y su raza es {perro.raza}")
    print(f"el nombre del gato es {gato.nombre} y su edad es de  {gato.edad}")

if __name__ == "__main__":
    main()
    
        

