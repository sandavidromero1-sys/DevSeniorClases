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
opcion = ""

print("-------Menu de opciones-------")
print("1. Opcion 1: saludar")
print("2. Opcion 2 : mensaje")
print("3. Opcion 3: salir")


while True:
    opcion = input("Ingrese una opcion (1-3): ")
    
    if opcion == "1":
        print("Hola, bienvenido al programa")
    elif opcion == "2":
        print("Este es un mensaje importante")
    elif opcion == "3":
        print("saliendo de la aplicacion...")
        break
    
