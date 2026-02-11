"""
Enunciado del ejercicio:

Una empresa tiene dos tiendas que venden productos distintos y, en algunos casos,coinciden en el inventario 
Escriba un programa en python que :

1. Reciba como conjuntos los productos dosponibles en la tienda "Tienda A" y en la tienda "Tienda B"
2. calcule y muestre:

 *"La union" de dos productos: todos los productos disponibles en ambas tiendas, sin duplicados.
 *La interseccion de productos : los productos que ambas tiene en comun
 *La diferencia de productos: los productos  que estan en la tienda A pero no en la Tienda B.

"""
def operaciones_productos(tienda_a:set,tienda_b:set):
    union = tienda_a|tienda_b
    interseccion = tienda_a & tienda_b
    diferencia = tienda_a - tienda_b 
    return union,interseccion,diferencia

def main():
    tienda_a = {"Laptop","Mouse","Teclado"}
    tienda_b = {"Mouse","Pantalla","Laptop"}
    
    union,interseccion,diferencia = operaciones_productos(tienda_a,tienda_b)
    
    print("Union: ", union)#Laptop,mouse,teclado,pantalla
    print("Interseccion",interseccion)#Mouse,laptop
    print("Diferencia",diferencia)#teclado
    
if __name__ == "__main__":
    main()
    