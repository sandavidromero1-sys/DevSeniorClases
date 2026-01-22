"""
listas = []
tuplas = ()
listas[tuplas()]
"""

colores = ["amarillo","azul","rojo"]
print(colores[2])
print(colores[1])

#tupla con valores diferentes
personal = ("Juan pablo", 22, True)

print(personal[0])
print(personal[2])

for color in colores:
    print(color)

# Desempaquetado de tuplas

nombre,edad,edo_civil = personal

print(nombre)
print(edad)
print(edo_civil)

#Tratado de modificar una tupla
persona = ("Juan pablo", 22, True)

#persona[1] = 29  no se puede cambiar la tupla 

persona = ("Juan pablo", 22, True)
