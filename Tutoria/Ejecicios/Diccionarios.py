#Diccionario para guardar la informacion de productos 
#nombre , id , precio y unidades en existencia 
# crear una funcion para modificar los datos del producto
#interactuando con el ususario en consola

productos = {
    
    "martillo":{
        "id":1,
        "precio":15000,
        "unidades":20},
    
    "destornillado":{
        "id":2,
        "precio":10000, 
        "unidades":15},
    
    "taladro":{
        "id":3,
        "precio":250000,
        "unidades":5},
    
    "mazo":{
        "id":4,
        "precio":20000,
        "unidades":10}
    
}

for clave,valor in productos.items():
    print(f"producto - {clave} valor - {valor}")
    
def buscar_producto(nombre):
    if nombre in productos:
        return productos[nombre]
    else:
        return None
def consultar_unidades(nombre):
    if nombre in productos:
        return f"Numero de unidade : {productos['martillo']['unidades']}"
    
busqueda = input("ingrese el nombre del producto a buscar: ")
resultado = buscar_producto (busqueda)
print(resultado)

print(f"Numero de unidade : {productos['martillo']['unidades']}")


