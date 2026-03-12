class edadInvalidaError(Exception):
    pass
class EdadNegativaError(Exception):
    pass
try:
    entrada = input("Ingrese su edad: ")
    if not entrada.isdigit():
        raise ValueError("Debe ingresar un numero entero")
    edad = int(entrada)
    
    if edad <= 0:
        raise EdadNegativaError("La edad no puede ser negativa")
except edadInvalidaError as e:
    print(f"Error de fromato:{e}")
except EdadNegativaError as e:
    print(f"Error logico:{e}")
else:
    print(f"La edad {edad} es valida")
finally:
    print("La ejecucion finalizo")
