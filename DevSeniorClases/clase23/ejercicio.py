"""
f = open("daros.txt" , "r") # leer
file1 = open("datos.txt" , "w")#limpiar
file2 = open("datos.txt" , "a")#agregar
file3 = open("datos.txt", "r+")#leer y escribir


with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
"""
with open("letras.txt", "w", encoding="utf-8") as f:
    f.write("A\n")
    f.write("B\n")
    f.write("C\n")
    f.write("D\n")
#metodo de lectura .read()
with open ("letras.txt","r", encoding="utf-8") as f:
    print(f.read())
#metodo .readline() es para leer una line a la vez
with open ("letras.txt","r", encoding="utf-8") as f:
    print(f.readline())
#metodo .readlines() imprime una lista de elementos contenidos en  el archivo
with open("letras.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()
#convencion 
#Nombre |apellido|edad
#Luis|molero|50

#Arquitectura minima p/manejo de archivos
#presentacion -> Interaccion con el usuario
#Servicio -> modelo/reglas del negocio
#Repositorio -> acceso a los datos
#Infraestructura -> archivos fisicos
#modelo/esquema ->datos
#super software

"""
1. FileManager (infraestructura segura)
2. Modelo task (serializacion)
3. repository (Persitencia desacoplo)
4. service (reglas de negocio + validaciones)
5. main (interfaz consola)
"""

# ToDo List

## Estándares de calidad
"""

| Norma                | Aplicación                         |
|----------------------|------------------------------------|
| PEP8                 | nombres, longitud, imports         |
| DRY                  | no repetir lógica de archivo       |
| KISS                 | funciones pequeñas                 |
| SRP                  | cada función hace una sola cosa    |
| Fail Fast            | validar antes de guardar           |
| Defensive Programming| proteger el archivo                |
| Inmutencia           | leer no modifica estado            |
| Encapsulación        | no acceder directo al archivo      |
| Tipado fuerte        | typing obligatorio                 |

"""





