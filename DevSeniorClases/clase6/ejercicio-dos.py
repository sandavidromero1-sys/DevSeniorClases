"""
Ciclos while - for
"""
# numero = 0

# while numero <= 5:
#  print(numero)
#  numero+=1
# print("Fin del ciclo")

"""    
While True
"""
# validacion de datos
# while True:
#     entrada = input("ingrese la hora (0-23): ")
    
#     if entrada.isdigit():
#         hora = int(entrada)
#         if hora>=0 and hora<=23:
#             break  
#     else:
#         print("Hora incorrecta, ingrese un valor entre 0 y 23")
       

# if hora>=0 and hora<=11:
#     print("Es la mañana")
    
# elif hora>=12 and hora<=17:
#     print("Es la tarde")
# elif hora>=18 and hora<=23:
#     print("Es la noche")

"""
### Calculadora de descuentos**

**Descripción:**
El usuario ingresa el valor de una compra.
Aplicar descuentos según la tabla:

| Monto         | Descuento |
| ------------- | --------- |
| ≥ 500000      | 20%       |
| 200000–499999 | 10%       |
| < 200000      | 0%        |

"""

# compra = float(input("Ingrese el valor de la compra: "))

# if compra>=500000 :
#     descuento = 0.2
#     descontado = compra * descuento
#     total = compra - descontado
# elif compra >= 200000 and compra <= 499999:
#     descuento= 0.1
#     descontado = compra * descuento
#     total = compra - descontado
# else:
#     descuento=0.0
#     descontado = compra * descuento
#     total = compra - descontado   
    
# print(f"El porcentaje de descuento fue {descuento * 100:.0f}% o {descontado:.2f}$ pesos" )
# print(f"Total a pagar {descontado:.2f}$")
 
"""
### Evaluador de presión arterial**

Descripción:
Ingresar la presión sistólica y diastólica, y clasificar el resultado.

| Condición                         | Mensaje |
| --------------------------------- | ------- |
| Sistólica < 90 o Diastólica < 60  | Baja    |
| Sistólica ≤ 120 y Diastólica ≤ 80 | Normal  |
| Sistólica > 120 o Diastólica > 80 | Alta    | 

"""

# while True: 
    
#     try:
#         sistolica = int(input("Ingrese la presión sistólica: "))
#         diastolica = int(input("Ingrese la presión diastólica: "))
        
#         # Validar de dartos de entrada
#         if sistolica <= 0 or diastolica <=0:
#             print("Los valores deben ser mayores a cero. Intente nuevamente.\n")
#             continue
#         if sistolica>300 or diastolica>200:
#             print("Los valores estan fuera del rango fisiologico.\n")
#             continue
#         break
        
#     except ValueError as e:
#         print("Error: Ingrese solo numero enteros\n")
        
# if sistolica < 90 or diastolica < 60:
#     print("Presión arterial baja")  
    
# elif sistolica <= 120 and diastolica <= 80:
#     print("Presión arterial normal")

# else:
#     print("Presión arterial alta !!! corre al hostpital")
    
    
"""
### Verificador de velocidad**

**Descripción:**
Pedir la velocidad de un vehículo y mostrar el estado.

| Velocidad (km/h) | Estado                 |
| ---------------- | ---------------------- |
| 0                | Detenido            |
| 1–60             | Velocidad normal    |
| 61–120           | Rápido               |
| >120             | Exceso de velocidad |

"""
# while True:
#     try:
#         velocidad = float(input("ingrese la velocidad del automovil: "))
        
#         if velocidad < 0 :
#             print("auto detenido ingrese un valor valido ")
#             continue
#         if velocidad > 200:
#             print("Valor fuera de un rago razonable")
#             continue
#         break
#     except ValueError:
#         print("Entrada no valida")
        
# if velocidad == 0:
#     print("El auto esta detenido")
# elif velocidad >= 1 and velocidad <= 60:
#     print("El auto esta en velocidad normal")
# elif velocidad >= 61 and velocidad <= 120:
#     print("El auto esta rapido")
# else:
#     print("El auto esta en exceso de velocidad")
    
"""

### Cálculo de impuesto según salario**

**Descripción:**
El usuario ingresa su salario mensual. Se aplica impuesto según rango:

| Rango               | Impuesto |
| ------------------- | -------- |
| ≤ 2.000.000         | 0%       |
| 2.000.001–5.000.000 | 10%      |
| > 5.000.000         | 20%      |
 
"""
while True: 
    try:
        salario = float(input("Ingrese su salario: "))
        if salario < 0:
            print(" Salario invalido.Ingrese un salario positivo")   
            continue
        break
            
    except ValueError :
        print("Entrada no valida")
     
if salario>=2000000 and salario<=5000000: 
    porcetajeIn = 0.1
    impuesto = salario * porcetajeIn
elif salario>5000000:
    porcetajeIn = 0.2
    impuesto = salario * porcetajeIn
    

else:
    print("No aplica debe aplica para impuesto")
    
print(f" *Su salario es de : {salario:.2f}$\n *tiene un porcentaje de impuesto de : {porcetajeIn:.2f}%\n *total a pagar {impuesto:.2f}\n")
    
    
   
    
        

        
