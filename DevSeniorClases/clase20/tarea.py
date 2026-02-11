"""
Ejercicio 1 — Eliminar datos duplicados
Una tienda registró varias veces el mismo producto en el sistema:
productos = ["pan", "leche", "huevos", "pan", "arroz", "leche", "pan"]
Actividad
1.	Convierte la lista en un set
2.	Muestra los productos únicos
3.	Indica cuántos productos diferentes existen
Qué debe aprender el estudiante: Un set se usa cuando no queremos repetidos
"""
# from typing import List
# def eliminar_duplicados(productos:List[str]) -> List[str]:
    
#     if not isinstance(productos,list):
#         raise TypeError("Se espera una listas ")
#     if not all (isinstance(p,str)for p in productos):
#         raise ValueError("Todos los elementos de la lista deben tener letras")
#     return sorted(set(productos))

# def main() -> None:
#     productos = ["pan", "leche", "huevos", "pan", "arroz", "leche", "pan"]
#     print("Lista original", productos)
    
#     try: 
#         resultado = eliminar_duplicados(productos)
#         print("Sin duplicados: ",resultado)
#     except(TypeError,ValueError) as error:
#         print(f"Error:{error}")
        
# if __name__ == "__main__":
#     main()   
    

"""
Ejercicio 2 — Verificar acceso (operador in)
Un sistema tiene usuarios autorizados:
usuarios_autorizados = {"ana", "carlos", "maria", "pedro"}
El programa debe pedir un nombre y decir si puede entrar o no.
Actividad
•	Solicitar un nombre con input
•	Indicar si pertenece al conjunto
Qué debe aprender el estudiante: Los sets permiten búsquedas extremadamente rápidas (mejor que lista)
# """
 
# def verficar_usuario (perfil,usuarios)-> str:
    
#     for  u in usuarios: 
#         if u == perfil:
#             return (f"!!!!Validacion Exitosa!!!!\n Puede ingresar {perfil}")
#     return (f"Acceso Denegado, vuelva a intentarlo {perfil}") 

# def main() -> None:

#     usuarios = {"ana", "carlos", "maria", "pedro"}
    
    
#     perfil = input(str("Ingrese su primer nombre: "))

#     resultado = verficar_usuario(perfil,usuarios)
#     print(resultado)
    
# if __name__ == "__main__":
#     main()
"""
Ejercicio 3 — Estudiantes en ambos cursos (intersección)
Dos profesores dictan cursos distintos:
python = {"Ana", "Luis", "Pedro", "Marta"}
java = {"Luis", "Carlos", "Ana", "Sofia"}
Actividad
Mostrar los estudiantes inscritos en ambos cursos
Concepto: intersección
"""
python = {"Ana", "Luis", "Pedro", "Marta"}
java = {"Luis", "Carlos", "Ana", "Sofia"}

print(python & java)

"""
Ejercicio 4 — Clientes exclusivos (diferencia)
Una empresa quiere saber qué clientes compraron solo online y no en tienda física
online = {"Juan", "Ana", "Pedro", "Lucia"}
tienda = {"Ana", "Pedro"}
Actividad
Mostrar clientes exclusivos online
Concepto: diferencia
"""
online = {"Juan", "Ana", "Pedro", "Lucia"}
tienda = {"Ana", "Pedro"}

print(online - tienda)

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
    