# texto= str(input("Ingrese un texto: "))
# cadena = ""

# for i in texto.lower():
#     if i  == "a":
#         cadena += "4"
#     elif i  == "e":
#         cadena += "3"
#     elif i  == "i":
#         cadena += "1"
#     elif i  == "o":
#         cadena += "0"
#     else:
#      cadena += i
     
    
# print(f"Resultdo: {cadena}")

signo = input("Ingrese la operacion (+,-,*,/)")
num1 = float(input("Ingrese el primer numero "))
num2 = float(input("Ingrese el segundo numero "))

if signo == "+":
    resultado = num1+num2
if signo == "-":
    resultado = num1-num2
if signo == "/":
    resultado = num1/num2
if signo == "*":
    resultado = num1*num2
    
print(F"El resultado es: {resultado}") 