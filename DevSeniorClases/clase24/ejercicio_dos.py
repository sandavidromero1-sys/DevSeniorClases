import csv
from pathlib import Path

FILE_PATH = Path("Inventario_dos.csv")

def create_inventario_file()-> None:
    fieldnames = ["id","nombre","precio","stock"]
    
    with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader()
        
        write.writerow(
            {
            "id":1,
            "nombre":"Mouse",
            "precio":10,
            "stock":100
             }
            )
        
        write.writerow(
            {
            "id":2,
            "nombre":"Teclado",
            "precio":25,
            "stock":50
             }
            )
        
        write.writerow(
            {
            "id":3,
            "nombre":"Monitor",
            "precio":200,
            "stock":20
             }
        )
        
def read_inventory() -> None:
    if not FILE_PATH.exists():
        print("El archivo no existe.")
        return
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\n*** Inventario ***\n")
        for row in reader:
            print(row)
def read_inventory_formatted() -> None:
    if not FILE_PATH.exists():
        print("El archivo no existe.")
        return
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\n*** Inventario  en Formato de salida***\n")
        for row in reader:
            print(f"ID: {row['id']} |"
                  f"Nombre: {row['nombre']} |"
                  f"Precio: ${row['precio']} |"
                  f"Stock: {row['stock']} unidades")
            
def main() -> None:
    create_inventario_file()
    read_inventory()
    read_inventory_formatted()
        
if __name__ == "__main__":
    main()
        
        
        
        
        