""" 
App que determina si una lista de numero tiene numeros pares o impares 
y los guarda los pares en una lista y los imapres en otra
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