"""
Funciones
"""
#funcion sin parametros ni retorno 
# def saludar():
#     print("Holaaa parce... (pana)")

# saludar()

# def salud2():
#     return "Holaaa parce... (pana)"
    
# print(salud2())

#Funcion con parametros 
# def saludo3(nombre):
#     print(f"Hola {nombre}, como estas?")
    
# saludo3("Andres")

# def suma(numeroUno:int,numeroDos:int)->int:
#     resultado = numeroUno + numeroDos
#     return print(f"La suma de {numeroUno} + {numeroDos} es {resultado}")

# suma(5,5)
# funciones con parametros con valores por defecto

# def presentar_estudiante (nombre:str,carrera:str = "Ingenieria de Sistemas")->str:
#     print(f"el estudiante es {nombre} y estudia {carrera}")
    
    
# presentar_estudiante("Juan","ingenieria civil")
# presentar_estudiante("Maria")


""" 
Estructuras de datos
list[] o List[] = mutables
Dict{} o dict{} = mutables
Tuple() o tuple() = inmutables

"""
#Funciones con efecto colateral
# estudiantes = []

# def agregar_estudiantes(nombre:str)->str:
#     estudiantes.append(nombre)
  
# agregar_estudiantes("Andres")
# print(f"Estudiantes: {estudiantes}")

"""
App que dermina si las medidas de una figura forman un triangulo
y de que tipo 
- Isoceles(dos lados iguales)
- Equilatero (todos los lados iguales)
- Escaleno(lados diferentes)
"""

# def triangulo(lado1:float , lado2 : float , lado3: float)->float:
#     if (lado1>lado2 and lado1>lado3):
#         mayor = lado1
#         menor1 =lado2
#         menor2 = lado3
#     elif (lado2>lado1 and lado2>lado3):
#         mayor = lado2
#         menor1 =lado1
#         menor2 = lado3
#     elif(lado3>lado1 and lado3>lado2 ):
#         mayor = lado3
#         menor1 =lado1
#         menor2 = lado2
        
#     Resultado = menor1 + menor2
#     if (Resultado > mayor):
#         print("Las medidas forman un triangulo")
#         if (lado1 == lado2 == lado3):
#             print("Es un triangulo equilatero")
#         elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
#             print("Es un triangulo isoceles")
#         else:
#             print("es un triangulo y Escaleno")
           
#     else:
#         print("Esas medidas no foman un triangulo")
        
        
    
    
# triangulo(8,6,10)
# print(triangulo)




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


        
        
 
 
 
 
