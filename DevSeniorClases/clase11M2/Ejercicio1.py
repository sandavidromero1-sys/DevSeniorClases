from dataclasses import dataclass

@dataclass
class Producto:
    _nombre: str
    _categoria: str
    _codigoInt: str
    _precioUnit: float
    _cantidad: int
    
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self,valor:str)-> None:
        if isinstance(valor,str) and valor.strip(): self._nombre = valor
        else:
            raise ValueError("El nombre debe ser un caracter. Por favor vuelva a intentar ")
    @property
    def categoria (self)-> str:
        return self._categoria
    @categoria.setter
    def categoria(self,valor:str) -> None:
        if isinstance(valor,str) and valor.strip(): self._categoria = valor
        else:
            raise ValueError("La categoria debe ser un caracter. Por favor vuelva a intentar ")
    @property
    def codigoInt (self)-> str:
        return self._codigoInt
    @codigoInt.setter
    def codigoInt(self,valor:str) -> None:
        if isinstance(valor,str) and valor.strip(): self._codigoInt = valor
        else:
            raise ValueError("El codigo debe ser un caracter. Por favor vuelva a intentar ")
    @property
    def precioUnit (self)-> float:
        return self._precioUnit
    @precioUnit.setter
    def precioUnit (self,valor:float) -> None:
        if isinstance(valor,float) and valor>0: self._precioUnit = valor
        else:
            raise ValueError("El precio debe ser un numero entero o en decimal mayor a 0")
    @property
    def cantidad (self)-> int:
        return self._cantidad
    @cantidad.setter
    def cantidad (self,valor:int) -> None:
        if isinstance(valor,int) and valor > 0: self._cantidad = valor
        else:
            raise ValueError("La cantidad debe ser un numero entero mayor a 0")
    def __repr__(self) -> str:
        return(
            f"Producto(Nombre='{self._nombre}', Categoria='{self._categoria}',"
            f"Codigo interno='{self._codigoInt}',Precio unitario='{self._precioUnit}',Cantidad='{self._cantidad}')"
        )
def main () -> None:
    producto1 = Producto("Tablet","Tecnologia","3432321",25000.00,20)
    producto2 = Producto("Cama","Hogar","34sdefe",2000.00,10)
    producto3 = Producto("Galletas","Comida","3efsfew32",3000.00,9)
    
    print("\n** Inventario de productos  \n")
    print(producto1)
    print(producto2)
    print(producto3)
    producto1.nombre = "Laptop"
    producto1.precioUnit = 305000.00
    producto3.codigoInt = "243idk22w"
    producto2.cantidad = 2
    
    print("\n*** Datos del inventario Actualizado\n")
    print(producto1)
    print(producto2)
    print(producto3)
    
    print("\n*** Inventario completo ***\n")

if __name__ == "__main__":
    main()
       
    
    
        
        
        
    