
#Operadores relacionales
#= ==

variablex = 5 
variabley = 10
variablea, variableb = 8,7

print(f'variablex == variabley:{variablex == variabley}')#->true o false
print(f'variablea != variableb:{variablea != variableb}')#->true o false
print(f'variablex > variabley:{variablex > variabley}')#->true o false
print(f'variablex <  variableb: {variablex < variableb}')#->true o false
print(f'variablea >= variableb:{variablea >= variableb}')#->true o false
print(f'varaiblex <= variabley:{variablex <= variabley}')#->true o false

    #operadores logicos
    #and, or, not
    

"""
    and = si tengo el viernes AND si tengo dinero =True
    or= si tengo el viernes Or si tengo dinero =True
"""
tienes_dinero = True
esta_libre = False

print(f"AND:{tienes_dinero and esta_libre}")
print (f"OR:{tienes_dinero or esta_libre}")
print(f"NOT:{not esta_libre}")

Nombre = "Juan"
Edad = 20
Cedula = "1234567890"

print(f'Mi nombre es :{Nombre} tengo {Edad} años y mi cedula es {Cedula}')

#Validacion manual 
edad = input("Ingrese su edad: ")
if edad.isdigit():
    
    edad= int(edad)
    print(f'Edad es valida: {edad}')
else:
    print("Error,por favor ingrese un numero entero positivo ")
    
tienes_dinero = False

if tienes_dinero:
    print("Puedes comprar el producto")
else:
    print("No puedes comprar el producto")
    
#Crear tres variables Booleanas

tienes_hambre = False
tienes_2Dinero = False

if tienes_hambre and tienes_2Dinero:
    print("Voy a comer en un resaurante")
    
elif tienes_hambre and not tienes_2Dinero:
    print("Voy a comer en mi casa")
    
else:
    print("No tengo hambre")
   

    """
    Operadores realcionales 
    
    Enunciado
    
    crear un programa para que el usuario ingrese dos numeros y muestre el resultado de las siguientes comparaciones
    
    si el primer numero es mayor que el segundo 
    
    si el primero numero es menor que el segundo
     
    si ambos son iguales 
    """
    numero1 = float(input("Ingrese un numero: "))
    numero2 = float(input("Ingrese otro numero: "))

if numero1>numero2:
    print(f'El numero {numero1} es mayor que {numero2}')
elif numero1 < numero2:
    print(f'El numero {numero1} es menor que {numero2}')
elif numero1 == numero2:
    print(f'El numero {numero1} es igual que {numero2}')
else:
    print("Error, ingrese numeros validos mayores a cero")
    
    #Ejercicio if
    
    edad_usuario = int(input("Ingrese su edad: "))
    #edad
    if edad_usuario>=18:
        print("Eres mayor de edad")
    else:
        print('Eres menor de edad')
    #numero positivo o negativo
    num = int(input("Ingrese un numero: "))
    if num>=0:
        print("El numero es positivo")
    else:
        print("El numero es negativo ")
    #rango de numero
    num2 = int(input("Ingrese un numero: "))
    if 10<num2<50:
        print("El numero esta en el rango")
    else:
        print("El numero no esta en el rango")
    
    