
"""
class Herramientas():
    def __init__(self, marca:str,color:str,peso:float,precio:float)->None:
        self.marca = marca
        self.color = color
        self.peso = peso
        self.precio = precio
    def mostra_info(self):
        print(f"\nmarca: {self.marca}, \ncolor:{self.color}, \nPeso: {self.peso},\nprecio: {self.precio}\n")
        
def main():
    herramienta1 = Herramientas("Stanley","Rojo",3.23,131232.00)
    herramienta1.mostra_info()

if __name__ == "__main__":
    main()
""" 
class Producto():
    def __init__(self,id,nombre,descripcion,precio,descuento,stock,cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.descuento= descuento
        self.stock = stock
        self.cantidad = cantidad
        
    def Rdescuento (self):
        return self.precio * (self.descuento/100)
    def StockHay(self,cantidad)-> bool:
     return self.stock >= cantidad
    def ReducirStock (self,cantidad)->bool:
        if StockHay (cantidad):
            self.stock -= cantidad
            return True
        return False
    def AgregarStock (self,cantidad)->None:
            self.stock += cantidad
    def PreciFin(self):
        return self.precio - self.Rdescuento()
    def obtener_info(self):
        print(f"Id:{self.id}, Nombre: {self.nombre} Descripcion: {self.descripcion}")
           
       
class Cliente():
    def __init__(self,id,nombre,direccion,compra,saldoFavor)-> None:
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.compra = compra
        self.saldoFavor = saldoFavor