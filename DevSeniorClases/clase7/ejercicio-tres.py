""" 
While contador
"""
# contador = 1

# while contador <= 5:
#     print("Hola Mundo")
#     contador += 1
    
# print("Fin del bucle")

#permitira solicitar un numero positivo por teclado y escribir "salir" para salir de la app
# palabra=""

# while  palabra!="salir":
#     palabra = input("Ingrese una palabra(salir... para terminar): ")
#     print(f"Usted ingreso la palabra: {palabra}")
    
# print("Fin del programa")

"""
menu de opciones por consola  
"""
# opcion = ""

# print("-------Menu de opciones-------")
# print("1. Opcion 1: saludar")
# print("2. Opcion 2 : mensaje")
# print("3. Opcion 3: salir")


# while True:
#     opcion = input("Ingrese una opcion (1-3): ")
    
#     if opcion == "1":
#         print("Hola, bienvenido al programa")
#     elif opcion == "2":
#         print("Este es un mensaje importante")
#     elif opcion == "3":
#         print("saliendo de la aplicacion...")
#         break
    
#Suma acumulada de numeros: Se solicita numeros al usuario y acumula su suma hasta que escriba 0.

# suma = 0 
# numero = int(input("Ingrese un numero (0 para terminar): "))

# while numero != 0:
#     suma += numero
#     numero = int(input("Ingrese un numero (0 para terminar): "))

# print(f"La suma acumulada es: {suma}")

#validar la entrada de un numero positivo: solicitar un numero positivo y repetir hasta que se ingrese uno valido.

# numero = int(input("Ingrese un numero positivo: "))
# while numero < 0:
#     print("Error: Debe ingresar un numero positivo.")
#     numero = int(input("te solicito que ingreses un numero positivo: "))

# print(f"Gracias! Ingreso el numero positivo: {numero}")

# for se utiliza para recorrer una secuencia (lista, cadena, rango, etc)
# imprimir numeros del 1 al 5
# for numero in range(1, 6): # se imprime del 1 al 5
#     print(f"Numero: {numero}")
    
#     #Ahora, quiero imprimir una lista de productos
# productos = ["manzana", "banana", "naranja", "pera"]

# for producto in productos:
#     print(f"Producto: {producto}")
    
    #el uso del "break" y el "continue" en un bucle for
    #brek: termina el bucle por completo
    
# for numero in range(1, 7):# se imprime del 1 al 6
#     if numero == 4:
#       print("Se interrumpio el ciclo for para excluir numeros mayores a 4")
#       break
#     print(f"El numero es: {numero}")

# continue: salta a la siguiente iteracion del bucle

# for numero in range(1, 7):# se imprime del 1 al 6
#     if numero == 4:
#         print("\n\n Por el uso de la PALABRA RESERVADA CONTINUE, se salta la impresion del numero 4\n\n ")
#         continue
#     print(f"El numero es: {numero}")
    
# for numero in range(1, 7, 2):# Se imprime del 1 al 6, pero de 2 en 2
#     print(f"\nEl numero es: {numero}\n")


"""
Imprimir una cadena de caracteres (String=>str) uno por uno utilizando un bucle for
"""
# caden = input ("Ingrese una cadena de texto: ")

# for caracter in caden:
#     print(f"{caracter}")
#Imprimir numeros del 1 al 100 utilizando un bucle for
for numero in range(1,101):
    print(f"Numero: {numero}")
    
#app que permita calcular el cuadrado delos numeros de 1 al 5
for numero in range(1,6):
    cuadrado = numero **2
    print(f"El numero que ingreso {numero} y su cuadrado es: {cuadrado}")
    
#app que permita mostrar solo las vocales de una cadena ingresada por el usuario
cadena1 = input("Ingrese una cadena de texto: ")
cadena = cadena1.lower() # Convertir a minusculas para facilitar la comparacion
vocales = "aeiou"
for caracter in cadena:
    if caracter in vocales:
        print(f"Vocal encontrada: {caracter}")
        
#app que permita imprimir la tabla de multiplicar de un numero ingresado por pantalla

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

for i in range (1 , 11):
    
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    
print("Fin de la tabla")
