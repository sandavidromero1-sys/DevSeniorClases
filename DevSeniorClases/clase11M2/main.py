from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float
    
    @property
    def titulo(self) -> str :
        return self._titulo
    
    @titulo.setter
    def titulo(self,valor:str)-> None:
        if isinstance(valor,str) and valor.strip():
            self._titulo = valor
        else:
            raise ValueError("El titulo debe ser un texto valido ")
        
    @property
    def autor(self)-> str:
        return self._autor
    @autor.setter
    def autor(self,valor:str) -> None:
         if isinstance(valor,str) and valor.strip():
            self._autor = valor
         else:
            raise ValueError("El autor debe ser un texto valido ")
    @property
    def isbn(self)->str:
        return self._isbn
    @isbn.setter
    def isbn(self,valor:str) -> None:
         if isinstance(valor,str) and valor.strip():
            self._isbn = valor
         else:
            raise ValueError("El isbn debe ser un texto valido ")
    @property
    def precio (self)-> float:
        return self._precio
    
    @precio.setter
    def precio (self,valor: float) -> None:
        if isinstance(valor,float) and valor > 0:
            self._precio = valor
        else:
           raise  ValueError("El precio debe ser un numero entero o con decimales")
       
    def __repr__(self) -> str:
        return(
            f"Libro(titulo='{self._titulo}', autor='{self._autor}',"
            f"ISBN='{self._isbn}',precio='{self._precio}')"
        )
        
def main () -> None:
    libro1 = Libro("Cien años de soledad","Gabo ","321-456-987-1",1000.00)
    
    print("\n** Informacion del libro \n")
    print(libro1)
    libro1.precio = 332424.000
    libro1.titulo = "100 Años de soledad"
    
    print("\n*** Datos de libro actualizados\n")
    print(libro1)
    
    print("\n*** Programa finalizado ***\n")
if __name__ == "__main__":
    main()
        
        
        
        
        
            