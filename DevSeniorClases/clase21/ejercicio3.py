"""
Enunciado

Desarrolle un programa en python que permita comprar los productos disponibles en dos tiendas.

el sistema debe solicitar por teclado los nombres de los productoa en la tienda "Tienda A" y la  "Tienda B",almacenamos en estructuras de tipo set[str].

implemente " todas las funciones necesarias con tipado fuerte (type hints)",incluye:
*una funcion para leer los productos por teclado
*una funcion que reciba conjuntos y retorne:

*La "union"
*La "interseccion"
*la "diferencia"(productos exclusivos de la tienda A)

finalmente, el programa principal debe iunvocar las funciones y mostrar los resultados obtenidos.
"""
from typing import Set, Tuple


def leer(tienda: str)->Set[str]:
    productos: Set[str] = set()
    print(f"Ingresar productos a {tienda} (Digite enter para terminar):")
    
    while True:
        pro = input(str("Escriba el producto: ")).strip().lower()
        if pro == "":
            break
        productos.add(pro)
    
    return productos


def operaciones_conjuntos_productos(a: Set[str], b: Set[str]) -> Tuple[Set[str], Set[str], Set[str]]:
    union: Set[str] = a | b
    interseccion: Set[str] = a & b
    diferencia_a: Set[str] = a - b
    diferencia_b: Set[str] = b - a
    return union, interseccion, diferencia_a,diferencia_b


def main() -> None:
    tienda_a: Set[str] = leer("Tienda A")
    tienda_b: Set[str] = leer("Tienda B")

    union, interseccion, diferencia_a,diferencia_b = operaciones_conjuntos_productos(tienda_a, tienda_b)

    print("\nConjunto A")
    print(tienda_a)
    print("\nConjunto B")
    print(tienda_b)
    print("\n--- OPERACIONES CON LOS CONJUNTOS  ---")
    print("-"*50)
    print("Unión:", union)
    print("-"*50)
    print("Intersección:", interseccion)
    print("-"*50)
    print("Diferencia en A:", diferencia_a)
    print("-"*50)
    print("Diferencia en B:", diferencia_b)


if __name__ == "__main__":
    main()
