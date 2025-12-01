
"""
from abc import ABC, abstractclassmethod
 
class Figura(ABC):

    @abstractclassmethod
    def calcular_area(slef):
        pass
    
class Circulo(Figura):
    def __init__(self, radio:float):
        self.radio = radio
        
    def calcular_area(self):
        area = 3.1416 * (self.radio ** 2)
        return area
        
    def calcular_radio(self):
        pass
    
    
    def calcular_perimetro(self):
        pass
    
def main ():
    figura1 = Circulo (5.0)
    print(f"El area del circulo es: {figura1.calcular_area():,.2f}")

if __name__ == "__main__":
    main()
"""
""" 
desarrolle una aplicacion que cree una clase abstracta  "Estudiante" y al menos 3 sub clases y como minimo  2 comportamientos/funciones.
"""
from abc import ABC, abstractmethod

class Estudiante(ABC):
    
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    
    @abstractmethod
    def pago(self, valor):
        pass


class Bachiler(Estudiante):
    def __init__(self, nombre, calificacion, grado):
        super().__init__(nombre, calificacion)
        self.grado = grado
        
    def calificar(self):
        print(f"\nEstudiante con el nombre: {self.nombre} "
              f"\ndel grado {self.grado} tiene una calificacion de {self.calificacion}")

    def pago(self, valor):
        print(f"\nEl valor a pagar por la colegiatura es {valor}")


class Pregrado(Estudiante):
    def __init__(self, nombre, calificacion):
        super().__init__(nombre, calificacion)

    
    def matricular(self, curso):
        print(f"\nEl estudiante {self.nombre} se matriculó en el curso {curso}")

    def pago(self, valor):
        print(f"\nEl valor a pagar es {valor}")

    def calificar(self, curso):
        print(f"\nTiene una calificación de {self.calificacion} en el curso {curso}")


class Postgrado(Estudiante):
    def __init__(self, nombre, calificacion, postgrado):
        super().__init__(nombre, calificacion)
        self.postgrado = postgrado 
    
    def matricula(self, curso):
        print(f"\nEstudiante con el nombre: {self.nombre} "
              f"\ninscrito en {self.postgrado}, tiene una calificación de {self.calificacion}")

    def pago(self, valor):
        print(f"\nEl valor pagado por el posgrado es {valor}")


def main():
    print("\nBachiller")
    estudiante1 = Bachiler("Ana", 4.5, "10mo")
    estudiante1.calificar()
    estudiante1.pago(500000)
    print("\nPregrado")
    estudiante2 = Pregrado("Luis", 3.8)
    estudiante2.calificar("Matemáticas")
    estudiante2.matricular("Programación")
    estudiante2.pago(1500000)
    print("\nPostgrado")
    estudiante3 = Postgrado("Maria", 4.2, "Maestría en Data Science")
    estudiante3.matricula("Big Data")
    estudiante3.pago(21324242)


if __name__ == "__main__":
    main()
