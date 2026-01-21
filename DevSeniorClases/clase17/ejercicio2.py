# Una tienda desea guardar la lista de nombres de sus clientes registrados para promociones
#el sistema debe poder:

# 1 Agregar nuevos clientes
# 2 recorrer la lista y mostrar todos 
# 3 Modificar un nombre en caso de error
# 4 Eliminar un cliente 

def agregar_cliente(Lista_clientes, nombre):
    
    if isinstance(nombre, str) and 2<= len(nombre) <= 50:
        Lista_clientes.append(nombre.title())
        print(f"Cliente agregado: {nombre}")
    else:
        print("Nombre invalido")
        
def mostrar_clientes(Lista_clientes):
    for cliente in Lista_clientes:
        print(cliente)

def modificar_cliente(Lista_clientes, indice, nuevo_nombre):
    if not (isinstance(nuevo_nombre, str)) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre invalido")
        return
    if 0 <= indice < len (Lista_clientes):
        Lista_clientes[indice] = nuevo_nombre.title()
        print(f"Cliente modificado - Nuevo nombre -> {nuevo_nombre}")
    else:
        print("Indice fuera del rango")
        
def eliminar_cliente(Lista_clientes, indice):
    if 0 <= indice < len(Lista_clientes):
        eliminado= Lista_clientes.pop(indice)
        print(f"cliente eliminado: {eliminado}")
    else:
        print("Indice fuera del rango")
        
def main():
    clientes = ["Andres","Cesar","Melany"]
    print("Clientes actuales:")
    mostrar_clientes(clientes)
    
    agregar_cliente(clientes, "Juan")
    
    modificar_cliente(clientes,0,"Santiago")
    
    eliminar_cliente(clientes,0)
    
    print("clientes actuales")
    mostrar_clientes(clientes)
    
if __name__ == "__main__":
    main()
        