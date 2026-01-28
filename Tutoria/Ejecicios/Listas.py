"""
carros = []
carros.append("ford")

print(carros)
carros.append("chevrolet")
print("carros")
carros.insert(0,"honda")
print(carros)
#insertar en posicion espesifica
carros.insert(2,"nissan")
print(carros)
print(len(carros))
carros.sort()
print(carros)
#ordenar de menor a mayor
carros.sort(reverse=True)
print(carros)

carros.reverse()
print(carros)
"""

#Programa de promedio de notas con listas 
asignaturas = []
datos = []

asignaturas.append("matematicas")
print(asignaturas)
asignaturas.append("fisica")
print(asignaturas)
asignaturas.append("quimica")
print(asignaturas)
#entrada de datos 
for asig in asignaturas:
    notas = []
    print(f"ingrse 3 notas pa para la asignatura de {asig}")
    for i in range(3):
        nota=float(input(f"nota{i+1}: "))
        notas.append(nota)
    
    datos.append([asig,notas])

#calculo

finalistas = []

for item in datos:
    promedio = sum(item[1])/len(item[1])
    print(f"Promedio en {item[0]}: {promedio:.2f}")
    
    if promedio>7:
        finalistas.append([item[0], promedio])
        
def segundo_elemento(x):
    return x[1]

finalistas.sort(key=segundo_elemento,reverse=True)

#con lamda
#finalistas.sort(key=segundo_elemento,reverse=True)

print("\n == Asignatura destacada (promedio > 7) ordenadas:===")

for nombre,promedio in finalistas:
    print(f"{nombre:<12} -> {promedio:.2f}")

# for f in finalistas:
#     print(f"{f[0]}: {promedio:.2f}")


