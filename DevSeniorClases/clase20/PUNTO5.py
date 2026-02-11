"""
Ejercicio 5 — Base de datos consolidada (unión + eliminación de repetidos)
Dos sucursales registraron clientes:
sucursal_1 = {"Carlos", "Maria", "Andres"}
sucursal_2 = {"Maria", "Luisa", "Carlos", "Elena"}
Actividad
Crear una base única de clientes sin duplicados
Concepto: unión
"""
from typing import Set
def DatosSin_Duplicados(sucursal_1,sucursal_2:Set) -> Set[str]:
    
    datos_unicos = (sucursal_1|sucursal_2)
    if not isinstance(datos_unicos,Set):
        raise TypeError("Se espera una Set")
    if not all (isinstance(d,str)for d in datos_unicos):
        raise ValueError("Todos los elementos de la lista deben tener caracteres")
    return sorted(set(datos_unicos)) 

def main() -> None:
    print("-" * 50)
    print("----- CLIENTES DE LA TIENDA ------")
    sucursal_1 = {"Carlos", "Maria", "Andres"}
    sucursal_2 = {"Maria", "Luisa", "Carlos", "Elena"}
    print(f"sucursal 1: {sucursal_1}\nsucursal 2: {sucursal_2}")
    
    try: 
        resultado = DatosSin_Duplicados(sucursal_1,sucursal_2)
        print("Clientes sin duplicados: ",resultado)
    except(TypeError,ValueError) as error:
        print(f"Error:{error}")
        
if __name__ == "__main__":
    main()   