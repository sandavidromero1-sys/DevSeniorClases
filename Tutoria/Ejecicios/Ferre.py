import os
import sys

class Cliente:
    def __init__(self,cedula, nombre, telefono, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        
    def obtener_resumen(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}, Teléfono: {self.telefono}, Dirección: {self.direccion}"

clientes_db = {
    "000": Cliente("1234567890", "Juan Pérez", "0987654321", "Av. Siempre Viva 123"),
    "001": Cliente("0987654321", "María Gómez", "0123456789", "Calle Falsa 456"),
}

def mostrar_cliente(cedula):
    print("\n---LISTA DE CLIENTES---")
    print(f"{'CÉDULA':<15} {'NOMBRE':<20} {'TELÉFONO':<15} {'DIRECCIÓN':<30}")
    print("-" * 80)
    for cliente in clientes_db.values():
        print(cliente.obtener_resumen())
    
def registrar_cliente():
    print("\n---REGISTRAR NUEVO CLIENTE---")
    cedula = input("Ingrese la cédula del cliente: ").strip()
    if cedula in clientes_db:
        print("El cliente ya está registrado.")
    else:
        nombre = input("Ingrese el nombre del cliente: ").strip()
        telefono = input("Ingrese el teléfono del cliente: ").strip()
        direccion = input("Ingrese la dirección del cliente: ").strip()
        
        nuevo_cliente = Cliente(cedula, nombre, telefono, direccion)
        clientes_db[cedula] = nuevo_cliente
        print(f"Cliente '{nombre}' registrado exitosamente.")  

inventario = {
    "001":{"nombre":"Martillo", "cantidad":50, "precio":15.99},
    "002":{"nombre":"Destornillador", "cantidad":80, "precio":7.49},
    "003":{"nombre":"Llave inglesa", "cantidad":30, "precio":12.89},
    "004":{"nombre":"Taladro", "cantidad":20, "precio":45.00},
}


factura_actual = []

def limpiar_pantall():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado_tabla():
    print (f"{'ID':<6} {'NOMBRE':<20} {'PRECIO':<10} {'STOCK':<8}")
    print("-" * 48)
    
def buscar_producto_nombre():
    print("\n---BUSCAR POR NOMBRE---")
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    
    encontrados= False
    print("\nResultado de busqueda: ")
    mostrar_encabezado_tabla()
     
    for id_prod, datos in inventario.items():
        if termino in datos["nombre"].lower():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:<9.2f} {datos['cantidad']:<8}")
            encontrados = True
    if not encontrados:
        print("No se encontraron productos con ese nombre.")
    print("-" * 48)
        
def mostrar_inventario():
    print("\n---INVENTARIO COMPLETO---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        mostrar_encabezado_tabla()
        for id_prod, datos in inventario.items():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:<9.2f} {datos['cantidad']:<8}")
        print("-" * 48)
        
def agregar_producto():
    print("\n---REGISTRAR NUEVO PRODUCTO---")
    id_producto = input("Ingrese el ID del producto: ").strip()
    if id_producto in inventario:
        print("El ID ya existe. No se puede agregar un producto con ese ID.")
    else:
        nombre= input("Ingrese el nombre del producto: ").strip()
        try:
            precio = float(input("Ingrese el precio unitario del producto: ").strip())
            cantidad = int(input("Ingrese la cantidad disponible: ").strip())
    
            inventario[id_producto] = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            print(f"Producto '{nombre}' agregado exitosamente.")
        except ValueError:
            print("Error: El precio debe ser un número y la cantidad un entero.")
            
def modificar_producto():
    print("\n---MODIFICAR PRODUCTO---")
    mostrar_inventario()
    id_producto = input("Ingrese el ID del producto a modificar: ").strip()
    if id_producto in inventario:
        prod = inventario[id_producto]
        print(f"Producto seleccionado: {prod['nombre']} (Stock: {prod['cantidad']}, Precio: ${prod['precio']:.2f})")
        print("1. Agregar Unidades (aumentar stock)")
        print("2. Modificar Precio")
        print("3. Cancelar")
        
        op_mod = input("Seleccione una opción: ")
        
        try:
            match op_mod:
                case "1":
                    cantida = int(input("¿Cuantas unidades desea agregar?: ").strip())
                    if cantida > 0:
                        prod["cantidad"] += cantida
                        print(f"Stock actualizado. Nueva cantidad de '{prod['nombre']}': {prod['cantidad']}")
                    else:
                        print("La cantidad a agregar debe ser un número positivo.")
                case "2":
                    nuevo_precio = float(input("Ingrese el nuevo precio: ").strip())
                    if nuevo_precio > 0:
                        prod["precio"] = nuevo_precio
                        print(f"Precio actualizado. Nuevo precio de '{prod['nombre']}': ${prod['precio']:.2f}")
                    else:
                        print("El precio debe ser un número positivo.")
                case "3":
                    print("Modificación cancelada.")
                case _:
                    print("Opción no válida.")
        except ValueError:
            print("Error: Entrada inválida.")
    else:
        print("El ID del producto no existe en el inventario.")
        
def vender_producto():
    print("\n---VENDER PRODUCTO---")
    mostrar_inventario()
    
    buscar = input("Desea buscar el ID por nombre antes (s/n)? ").strip().lower()
    if buscar == 's':
        buscar_producto_nombre()
    
    id_producto = input("Ingrese el ID del producto a vender: ").strip()
    
    if id_producto in inventario:
        prod = inventario[id_producto]
        print(f"Producto seleccionado: {prod['nombre']} (Stock: {prod['cantidad']}, Precio: ${prod['precio']:.2f})")
        try:
            cantidad_vender = int(input("Ingrese la cantidad a vender: ").strip())
            if 0 < cantidad_vender <= prod['cantidad']:
                subtotal = cantidad_vender * prod['precio']
                factura_actual.append({
                    "id": id_producto,
                    "nombre": prod['nombre'],
                    "cantidad": cantidad_vender,
                    "precio_unit": prod['precio'],
                    "subtotal": subtotal
                })
                prod['cantidad'] -= cantidad_vender
                print(f"Producto '{prod['nombre']}' agregado a la factura. Subtotal: ${subtotal:.2f}")
            else:
                print("Cantidad inválida o insuficiente en stock.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
        
def eliminar_producto():
    print("\n---ELIMINAR PRODUCTO---")
    mostrar_inventario()
    id_producto = input("Ingrese el ID del producto a eliminar: ").strip()
    if id_producto in inventario:
        print(f"Producto seleccionado para eliminación: {inventario[id_producto]['nombre']}")
        confirmacion = input("¿Está seguro que desea eliminar este producto? (s/n): ").strip().lower()
        if confirmacion == 's':
            eliminado = inventario.pop(id_producto)
            print(f"Producto '{eliminado['nombre']}' eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("El ID del producto no existe en el inventario.")
        
def generar_factura():
    print("\n" + "=" * 40)
    print(" Ferretería El Tornillo Feliz - FACTURA")
    print("Factura de venta ")
    print("=" * 40)
    
    if not factura_actual:
        print("No se han registrado ventas en esta sesión.")
    else:
        total = 0
        print(f"{'CANT.':<6} {'PRODUCTO':<20} {'PRECIO UNIT.':<15} {'SUBTOTAL':<10}")
        print("-" * 55)
        for item in factura_actual:
            print(f"{item['cantidad']:<6} {item['nombre']:<20} ${item['precio_unit']:<14.2f} ${item['subtotal']:<9.2f}")
            total += item['subtotal']
        print("-" * 45)
        print(f"{'TOTAL A PAGAR:':<42} ${total:.2f}")
        print("=" * 40 )
        
        if input("\n ¿confirmar pago y cerrar venta? (s/n): ").lower() == 's':
            factura_actual.clear()
            print("Venta cerrada y factura generada.")
            
def main():
    while True:
        print("\n---SISTEMA DE GESTIÓN DE FERRETERÍA---")
        print("1. Mostrar Inventario")
        print("2. Buscar Producto por Nombre")
        print("3. Vender (agregar a factura)")
        print("4. Generar Factura")
        print("-" * 30)
        print("5. Agregar Nuevo Producto")
        print("6. Modificar Producto")
        print("7. Eliminar Producto")
        print("8. Salir")
        
        opcion = input("\n>>Seleccione una opción: ")
        
        match opcion:
            case "1":
                mostrar_inventario()
            case "2":
                buscar_producto_nombre()
            case "3":
                vender_producto()
            case "4":
                generar_factura()
            case "5":
                agregar_producto()
            case "6":
                modificar_producto()
            case "7":
                eliminar_producto()
            case "8":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")
        limpiar_pantall()
        
if __name__ == "__main__":
    if sys.version_info < (3, 10):
        print("Este programa requiere Python 3.10 o superior.")
    else:
        main()