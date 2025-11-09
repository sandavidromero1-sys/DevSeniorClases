App de Números Pares e Impares

Esta aplicación en Python permite determinar si los números de una lista son pares o impares, y los guarda en listas separadas para cada tipo. Es un ejemplo simple y didáctico de uso de estructuras de control, listas y funciones en Python.
------------------------------------------------------------------------------------
Características

- Clasifica automáticamente los números de una lista.

- Guarda los pares y impares en listas independientes.

- Muestra cuántos números contiene la lista original.

- Código limpio, comentado y fácil de entender.
--------------------------------------------------------------------------------------
Ejemplo de uso:

""" 
App que determina si una lista de numeros tiene numeros pares o impares 
y guarda los pares en una lista y los imapres en otra
"""
#Lisas Inicialisadas
lista = [1,2,3,4,5,6,7,8,9,10]
pares = []
inpares = []
#Se crea la funcion donde se hace el proceso para determinar si el numeros es par o impar y 
#agregarlo a la lista de pares o impares 
def listParInpar ():
 print(f"Hay {len(lista)} numeros en la lista")
 #For que recorre la lista desde el primero hata el ultimo lemento 
 for i  in lista:
#If este calcula el modulo de cada numero de la lista y determina si es par o impar y los agrega a la lista correspondiente
    if i % 2 == 0 :
            pares.append(i)
    else:
            inpares.append(i)            
#Se imprime la lista con los numeros pares e impares   
 print(f"Los numeros pares de la lista son: {pares}")
 print(f"Los numeros inpares de la lista son: {inpares}") 
 
#Se ejecuta la funcion para visualizar los resultados 
listParInpar() 
--------------------------------------------------------------

Ejemplo de salida:
Hay 10 numeros en la lista
Los numeros pares de la lista son: [2, 4, 6, 8, 10]
Los numeros inpares de la lista son: [1, 3, 5, 7, 9]
------------------------------------------------------------
Autor

Santiago Romero M.
Proyecto educativo para practicar Python básico.