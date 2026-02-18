# #devolver una lista sn elementos repetidos y de mayort a menor

# numeros = [4, 2, 7, 2, 9, 4, 1]
# salida = []

# for num in numeros:
#     if num not in salida:
#         salida.append(num)

# salida.sort(reverse=True)
# print(salida)


# #dar los que no estan repetidos

# datos= [10,20,10,30,40,20,50]
# resultado = []
# for item in datos:
#     if item not in resultado:
#         resultado.append(item)
        
# print(len(resultado))

# cantidad_unica = len(set(datos))

# print(cantidad_unica)

#dada una lista de 70 numero del 1 al 100 devolver una lista con los numero que hacen falta 

import random

# numeros = random.sample(range(1, 101), 70)
# print(numeros)

# lista =[70, 99, 88, 66, 15, 48, 55, 18, 73, 7, 44, 94, 71, 80, 81, 90, 26, 37, 19, 79, 100, 97, 58, 62, 11, 14, 91, 39, 74, 93, 12, 9, 75, 25, 16, 1, 23, 4, 78, 83, 31, 96, 98, 24, 54, 85, 84, 8, 35, 36, 17, 40, 38, 95, 29, 86, 77, 87, 76, 57, 50, 49, 47, 3, 69, 51, 5, 63, 65, 42]
# lista.sort()

# numeros_completos = list(range(1, 101))

# lista_set=set(lista)
# faltantes=set(numeros_completos)-lista_set
# print("los numeros faltantes son: ", sorted(faltantes))

listas = [1,2,3,2,3,3,4,4,5,5,5]

resultado= []

for elemento in listas:
    if listas.count(elemento) == 2 and elemento not in resultado:
        resultado.append(elemento)

print(resultado)
