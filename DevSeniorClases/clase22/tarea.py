from typing import Set

libros = {
    "L1": {"nombre": "El principito", "Estado": True},
    "L2": {"nombre": "1984", "Estado": False},
    "L3": {"nombre": "Los juegos del hambre", "Estado": True},
    "L4": {"nombre": "El club de la pelea", "Estado": False},
    "L5": {"nombre": "El resplandor", "Estado": True},
    "L6": {"nombre": "It", "Estado": False},
}

prestamos = {}


def buscar_libro_por_nombre():
    termino = input("Ingrese nombre o parte del nombre del libro: ").strip().lower()
    encontrados = []

    for codigo, datos in libros.items():
        if termino in datos["nombre"].lower():
            encontrados.append(codigo)
            estado = "Disponible" if datos["Estado"] else "Prestado"
            print(f"{codigo} - {datos['nombre']} ({estado})")

    if not encontrados:
        print("No se encontró ningún libro.")

    return encontrados


def prestar_libro():
    doc = input("Ingrese su documento: ").strip()

    print("\n¿Cómo desea buscar el libro?")
    print("1. Por código")
    print("2. Por nombre")

    opcion = input("Seleccione una opción: ").strip()
    codigo = None

    if opcion == "1":
        print("\nEstado de todos los libros:")
        print("-" * 40)

        for codigo, datos in libros.items():
            estado = "Disponible" if datos["Estado"] else "Prestado"
            print(f"{codigo} - {datos['nombre']} ({estado})")
        print("-" * 40)
        codigo = input("Ingrese el código del libro: ").strip().upper()

    elif opcion == "2":
        resultados = buscar_libro_por_nombre()
        if resultados:
            print("\nEstado de todos los libros:")
        print("-" * 40)

        for codigo, datos in libros.items():
            estado = "Disponible" if datos["Estado"] else "Prestado"
            print(f"{codigo} - {datos['nombre']} ({estado})")
            print("-" * 40)
            codigo = input("Ingrese el código del libro a prestar: ").strip().upper()
        else:
            return
    else:
        print("Opción no válida.")
        return

    if codigo not in libros:
        print("El libro no existe.")
        return

    if not libros[codigo]["Estado"]:
        print("El libro ya está prestado.")
        return

    if doc not in prestamos:
        prestamos[doc] = set()

    if codigo in prestamos[doc]:
        print("El estudiante ya tiene este libro.")
        return

    prestamos[doc].add(codigo)
    libros[codigo]["Estado"] = False
    print(f"Libro '{libros[codigo]['nombre']}' prestado al estudiante {doc}.")


def devolver_libro():
    doc = input("Ingrese su documento: ").strip()
    codigo = input("Ingrese el código del libro a devolver: ").strip().upper()

    if doc not in prestamos or codigo not in prestamos[doc]:
        print("Error: el estudiante no tiene este libro.")
        return

    prestamos[doc].remove(codigo)
    libros[codigo]["Estado"] = True
    print(f"Libro '{libros[codigo]['nombre']}' devuelto correctamente.")

    if not prestamos[doc]:
        del prestamos[doc]


def ver_libros_estudiante():
    doc = input("Ingrese su documento: ").strip()

    if doc not in prestamos or not prestamos[doc]:
        print("El estudiante no tiene libros prestados.")
        return

    print(f"\nLibros del estudiante {doc}:")
    for codigo in prestamos[doc]:
        print(f"{codigo} - {libros[codigo]['nombre']}")


def ver_estado_libros():
    print("\nEstado de todos los libros:")
    print("-" * 40)

    for codigo, datos in libros.items():
        estado = "Disponible" if datos["Estado"] else "Prestado"
        print(f"{codigo} - {datos['nombre']} ({estado})")

    print("-" * 40)


# =============================
# MENÚ PRINCIPAL
# =============================

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Ver libros de un estudiante")
        print("4. Ver estado de todos los libros")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                prestar_libro()
            case "2":
                devolver_libro()
            case "3":
                ver_libros_estudiante()
            case "4":
                ver_estado_libros()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
