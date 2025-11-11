"""
Proyecto practico integrado 

Descripcion: crear una palicacion modular que permita :

1. Registrar estudiantes 
2.mostrar todos los registros
3.Buscar estudiante por nombre 
4.calcular promedio general
5. validar entradas y salidas

"""

#lista
estudiantes = []

def registrar_estudiante():
    print("\n--- Registrar estudiantes ----")
    nombre = input("Nombre:").strip().title()
    edad = int(input("Edad: "))
    nota = float(input("Nota (0 - 5):"))
    
    estudiante = {"nombre":nombre,"edad":edad,"nota":nota}
    estudiantes.append(estudiante)
    print("Estudiante registrado satisfactoriamente ")
    
def mostrar_estudiante():
    print("\n--- Lista de estudiantes ---")
    if not estudiantes:
        print("No hay estudiantes registrados ")
    else:
        for i, e in enumerate(estudiantes,1):
            print(f"{i}. {e['nombre']} - {e['edad']} años - Nota:{e['nota']}") 
    
def buscar_estudiante():
    print("\n---Buscar un estudiante ---")
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()
    #Funcion lamda = Express y desechable 
    encontrados = [ e for e in estudiantes if nombre in e ["nombre"].lower() ]
    
    if encontrados:
        for e in encontrados:
            print(f"{i}. {e['nombre']} - {e['edad']} años - Nota:{e['nota']}") 
    else:
        print("No se encontro ningun estudiante registrado. ")
    
    
