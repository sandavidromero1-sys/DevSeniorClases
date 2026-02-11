"""
Ejercicio 1 — Eliminar datos duplicados
Una tienda registró varias veces el mismo producto en el sistema:
productos = ["pan", "leche", "huevos", "pan", "arroz", "leche", "pan"]
Actividad
1.	Convierte la lista en un set
2.	Muestra los productos únicos
3.	Indica cuántos productos diferentes existen
Qué debe aprender el estudiante: Un set se usa cuando no queremos repetidos
"""
from typing import List
def eliminar_duplicados(productos:List[str]) -> List[str]:
    
    if not isinstance(productos,list):
      raise TypeError("Se espera una listas ")
    if not all (isinstance(p,str)for p in productos):
        raise ValueError("Todos los elementos de la lista deben tener letras")
    return sorted(set(productos))

def main() -> None:
    productos = ["pan", "leche", "huevos", "pan", "arroz", "leche", "pan"]
    print("Lista original", productos)
    
    try: 
        print("-" * 50)
        print("---- PRODUCTOS DEL MERCADO ----")
        resultado = eliminar_duplicados(productos)
        print(f"Sin duplicados:  {resultado}\nExisten {len(productos)} productos diferentes.")
    except(TypeError,ValueError) as error:
        print(f"Error:{error}")
        
if __name__ == "__main__":
    main()   