
"""
Clasificador de temperatura

Solicitar la temperatura


"""

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura < 0:
    print("Hace mucho frío")
elif 0 <= temperatura < 20:
    print("Clima templado")
elif 21 <= temperatura < 30:
    print("Clima Agradable")
else:
    print("Terribelmente caluroso")
    
    
#Progrma que valida si unapersona es mayor de edad o no
edad = int(input("Ingrese su edad: "))

if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""
Ejercicios:

1. Número positivo, negativo o cero

Descripción: Solicitar un número e indicar si es positivo, negativo o cero.

2. Clasificador de notas

Descripción: El usuario ingresa una nota de 0 a 100. Mostrar el nivel académico según el puntaje.

| Rango  | Mensaje   |
| ------ | ----------|
| 90–100 | Excelente |
| 70–89  | Aprobado  |
| 0–69   | Reprobado |


3. Clasificador de edad

Descripción: Pedir la edad del usuario y clasificarla en rangos.

| Rango | Mensaje      |
| ----- | ------------ |
| 0–12  | Niño         |
| 13–17 | Adolescente  |
| 18–59 | Adulto       |
| 60+   | Adulto mayor |


4. Verificar hora del día

Descripción: Pedir la hora (0 a 23) e indicar si es mañana, tarde o noche.

"""
#Ejercicio 1: Número positivo, negativo o cero
numero = float(input("Ingrese un numero"))

if numero < 0:
    print("El numero es negativo ")
elif numero > 0:
    print("El numero es positivo")
else:
    print("El numero es cero ")

#Ejercicio 2: Clasificador de notas
nota = float(input("Ingrese su nota (0-100): "))
if 0 <= nota <=69:
    print("Reprobado su nota es" + nota  )
elif 70 <= nota <=89:
    print("Aprobado")
elif 90 <= nota <=100:
    print("Excelente")
else:
    print("Nota invalida")
    
#Ejercicio 3: Clasificador de edad
ed = int(input("Ingrese su edad: "))

if 0 <= ed <=12:
    print("Niño")
elif 13 <= ed <=17:
    print("Adolescente")
elif 18 <= ed <=59:
    print("Adulto")
elif ed >=60:
    print("Adulto mayor")
    
#Ejercicio 4: Verificar hora del día
hora = int(input("Ingrese la hora (0-23): "))

if 0<= hora <12:
     print("Mañana")
elif 12 <= hora <18:
        print("Tarde")
elif 18 <= hora < 24:
        print("Noche")