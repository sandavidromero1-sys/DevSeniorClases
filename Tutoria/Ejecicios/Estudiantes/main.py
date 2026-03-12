from repositories.estudiante_repository_csv import EstudianteRepositoryCSV
from models.estudiante import Estudiante

def main():
    # Crear un repositorio de estudiantes
    repo = EstudianteRepositoryCSV()

    while True:
        print("\n1. Agregar estudiante")
        print("2. Listar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Generar lista de supermercado")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # Agregar estudiante
            id = int(input("Ingrese el ID del estudiante: "))
            nombre = input("Ingrese el nombre: ").strip()
            apellido = input("Ingrese el apellido: ").strip()
            edad = int(input("Ingrese la edad: ").strip())
            
            estudiante = Estudiante(id, nombre, apellido, edad)
            repo.agregar(estudiante)
            print(f"Estudiante {nombre} agregado correctamente.")
        
        elif opcion == "2":
            # Listar estudiantes
            estudiantes = repo.listar()
            if estudiantes:
                print("\nLista de estudiantes:")
                for est in estudiantes:
                    print(f"ID: {est.id}, Nombre: {est.nombre} {est.apellido}, Edad: {est.edad}")
            else:
                print("No hay estudiantes registrados.")
        
        elif opcion == "3":
            # Eliminar estudiante
            id = int(input("Ingrese el ID del estudiante a eliminar: "))
            eliminado = repo.eliminar(id)
            if eliminado:
                print(f"Estudiante con ID {id} eliminado correctamente.")
            else:
                print(f"No se encontró el estudiante con ID {id}.")
        
        elif opcion == "4":
            # Generar lista de supermercado
            repo.generar_lista_supermercado_txt()
            print("Lista de supermercado generada correctamente.")
        
        elif opcion == "5":
            # Salir
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()