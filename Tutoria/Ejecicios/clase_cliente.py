class Cliente():
    def __init__(self,nombre,cedula,telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        
cliente1 = Cliente("Juan Perez","1234567890","555-1234")
cliente2 = Cliente("Maria Gomez","0987654321","555-5678")
clientes = {}

nombre = input("Ingrese el nombre del cliente: ")
cedula = input("Ingrese la cédula del cliente: ")
telefono = input("Ingrese el teléfono del cliente: ")

nuevo_cliente = Cliente(nombre, cedula, telefono)
        
clientes["001"] = {
    "nombre": cliente1.nombre,
    "telefono": cliente1.telefono,
    "cedula": cliente1.cedula
}
clientes["002"] = {
    "nombre": cliente2.nombre,
    "telefono": cliente2.telefono,
    "cedula": cliente2.cedula
}

clientes["003"] = {
    "nombre": nuevo_cliente.nombre,
    "telefono": nuevo_cliente.telefono,
    "cedula": nuevo_cliente.cedula
}
print(clientes)     

for clave, valor in clientes.items():
    print(f"CLIENTE: {clave}")
    for k, v in valor.items():
        print(f"  {k}: {v}")  