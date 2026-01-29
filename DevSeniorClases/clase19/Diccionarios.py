#algun ejemplo de diccionario (dict)

persona = {"nombre":"Luis","edad":50,"residencia":"Colombia"}

persona = {
    "nombre": "Luis",
    "edad": 50,
    "residencia": "Colombia"
}

cliente = dict(
    nombre="Luis",
    telefono="123443234"
)
#Imprimir elemento del diccionario 
print(cliente["nombre"])
print(cliente.get("telefono"))

paciente = {"nombre":"Santiago", "especie":"perro", "edad": 5,"vacunado":True}

#Uso del metodo .keys()

print("Claves registradas en el diccionario")

for clave in paciente.keys():
    print(f"Claves disponibles {clave}")
    
print("Valores disponibles en el diccionario")

for valor in paciente.values():
    print(f" Valores disponibles {valor}")
    
print("\nRegistro completo de pacientes registrados\n")

for clave,valor in paciente.items():
    print(f"Clave: {clave} - Valor: {valor}")
    
#Actualizar un registro de diccionario

print("\nActualizacion del registro del paciente\n")
paciente.update({"especie": "canino","edad": 5,"vacunado":False})
for clave,valor in paciente.items():
    print(f"clave: {clave} - valor: {valor}" )
    
#Eliminar registro pero antes lo mostramos con POP
print("\nActualizacion del registro del paciente(eliminar registro)\n")
dato_eliminado = paciente.pop("vacunado",False)
print(dato_eliminado)
print(paciente)


    
