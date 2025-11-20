"""
class libro:
    #Metodo constructor
    def __init__(self,titulo, autor, isbn, precio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.precio = precio
        
libro1 = libro("Matematicas","Juan Guerra","231223213-43",90800)
print(libro1.titulo)
print(libro1.autor)

"""

#ERROR Encapsulamiento

# class Libro:
#     def __init__(self, titulo, precio):
#         self.titulo = titulo
#         self.precio = precio
        
# libro2 = Libro("Sthepen King", 20800)

# libro2.precio = 250
# print(libro2.precio)
        
#Encapsulamiento correcto

# class Libro:
#     def __init__(self,titulo,precio):
#         self.__precio = precio
#         self.__titulo = titulo
        
#     def get_precio(self):
#         return self.__precio
#     def set_precio(self,nuevo_precio):
#         # validar el precio
#         if isinstance(nuevo_precio, (int,float)) and nuevo_precio > 0 :
#             self.__precio = nuevo_precio
#         else:
#             print("ERROR al ingresar el precio del libro ")
#     def mostrar_info(self):
#         print(f"Titulo: {self.__titulo}")
#         print(f"Precio: {self.__precio}")
        
# def main():
#     print("\n*** SISTEMA DE REGISTRO DE LIBROS ***")
    
#     book1 = Libro("Biologia",1000)
#     print("Informacion del libro")
    
#     #Mostrar informacion actual del objeto/instancia
#     book1.mostrar_info()
    
#     #mostrar el precio actual 
#     print("Precio actual: ", book1.get_precio())
    
#     #Cambiar el valor actual del libro ERROR
#     book1.set_precio(-100)
    
#     # Cambiar nombre actual del libro 
#     book1.set_precio(2000)
    
#     print("Nuevo precio: ", book1.get_precio)
    
#     print("\n Software IA finalizado ")
    
#     if __name__ == "__main__":
#         main()
        
# Encapsulamiento correcto
"""
class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        # validar el precio
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("ERROR al ingresar el precio del libro")
        
    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Precio: {self.__precio}")

def main():
    print("\n*** SISTEMA DE REGISTRO DE LIBROS ***") 
    
    book1 = Libro("Biología", 1000)
    
    print("Información del libro")
    
    # Mostrar información actual del objeto/instancia/ejemplar
    book1.mostrar_info()
    
    # mostrar el precion actual
    print("Precio actual:", book1.get_precio())
    
    # Cambiar el precio actual del libro (ERROR)
    book1.set_precio(-1500)
    
    # Cambiar nuevamente el precio actual del libro
    book1.set_precio(2000)
    
    print("Nuevo precio: ", book1.get_precio())
    
    print("\n Software IA finalizado")

if __name__ == "__main__":
    main()
"""
#Mejor calidad de codigo 
"""
class Libro:
    
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("ERROR al ingresar el precio del libro")
    
    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Precio: {self.__precio}")
    
def main():
    print("\n*** SISTEMA DE REGISTRO DE LIBROS ***") 
    
    book1 = Libro("Biología", 1000)
    
    print("Información del libro")
    
    # Mostrar información actual del objeto/instancia/ejemplar
    book1.mostrar_info()
    
    # mostrar el precio actual
    print("Precio actual:", book1.precio)
    
    # Cambiar el precio actual del libro (ERROR)
    book1.precio = 2000
    
    print("Nuevo precio: ", book1.precio)
    
    print("\n Software IA finalizado")

if __name__ == "__main__":
    main()
"""

#Ejercicio de clase
class Auto:
    
    def __init__(self,precio,modelo,anio):
        self.__precio = precio
        self.__modelo = modelo
        self.__anio = anio
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("ERROR, Ingrese un precio valido para el automovil")
    
    @property
    def anio(self):
        return self.__anio
    
    @anio.setter
    def anio(self,nuevo_año):
        if isinstance(nuevo_año, (int)) and nuevo_año > 0:
            self.__anio = nuevo_año
        else:
            print(" Error,Ingrese un año positivo ")
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,nuevo_modelo):
        if isinstance(nuevo_modelo, (str)) :
            self.__anio = nuevo_modelo
        else:
            print("Error, Solo letras  ")
    
    def mostrar_info(self):
        print(f"\nModelo: {self.__modelo}")
        print(f"Precio: {self.__precio}")
        print(f"Año: {self.__anio}")
        
def main():
    print("\n*** SISTEMA DE REGISTRO DE AUTOMOVILES ***") 
    
    Auto1 = Auto(24000, "Logan",2014)
    
    print("Información del auto")
    
    # Mostrar información actual del objeto/instancia/ejemplar
    Auto1.mostrar_info()
    
    
    Auto1.precio = 30500
    Auto1.anio =2050
    Auto1.modelo ="Duster"
    
    # mostrar Atributos Actuales
    Auto1.mostrar_info()
   
    
    print("\n Software finalizado")

if __name__ == "__main__":
    main()