# try:
#     #bloque de codigo
# except ValueError:
#     #codigo  
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("debe ingresar un numero entero")
    

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("debe ingresar un numero entero")
except TypeError:
    print("debe ingresar un numero entero")
except Exception as e:
    print("Ocurrio un error: ", e)
    
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("debe ingresar un numero entero")
else:
    print("La ejecucion dio un resultado positivo(else)")
finally:
    print("La ejecucion finalizo (finally)")
    