# Ejercicios: I

"""
Slicing:
Dada la lista:

empleados = ["Ana", "Luis", "Carlos", "Marta", "Diana"]

Hacer:
1. Extrae los elementos desde "Luis" hasta "Marta" (inclusive).
2. Extrae los elementos el primero y el último.
"""
empleados = ["Ana", "Luis", "Carlos", "Marta", "Diana"]

extraer_elementos =  empleados[1:4]
extrar_prim_ult = [empleados [0],empleados[-1]]

print(f"elementos desde Luis hasta Marta:\n{extraer_elementos}")
print(f"el primer y ultimo elemento son:\n {extrar_prim_ult}")

"""
Slicing con pasos (step)
Dada la lista:  

datos = [1, 2, 3, 4, 5, 6, 7, 8]

Hacer:
1. Obtén los elementos en posiciones pares.
2. Obtén los elementos en posiciones impares.
"""
datos = [1, 2, 3, 4, 5, 6, 7, 8]
pares = []
impares = []

for i in range(len(datos)):
    if i % 2 == 0:
        pares.append(datos[i])
    else:
        impares.append(datos[i])

print(f"numero con indices pares:\n {pares}")
print(f"numero con indices impares:\n {impares}")
