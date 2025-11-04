""" 
Solicitar un numero(if)
"""
# while True:
#     numero = int(input("ingrese un numero: "))
#     try:
#         if numero < 0:
#             print("Error: El numero no puede ser negativo.")
#             continue
#     except ValueError as e:
#         print("Error: Debe ingresar un numero valido.")
#     break


# if numero > 50:
#     print("El numero es mayor a 50")
# elif numero == 50:
#     print("El numero es igual a 50")
# else:
#     print("El numero es menor a 50")
    
""" 
while
    
"""
numero = 1
while numero == 1:
    Respuesta = str(input("quiere salir o continuar (s/c): "))
    if Respuesta == "c":
        print("Gracias por continuar")
        continue
    elif Respuesta == "s":
        print("Saliendo de la App")
        numero = 0
    else:
        print("Digite una opcion valida")
