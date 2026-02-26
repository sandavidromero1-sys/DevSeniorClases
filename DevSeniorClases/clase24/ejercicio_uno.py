import csv 
from pathlib import Path

FILE_PATH = Path("inventario.csv")

def create_inventory_file() -> None:
    with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)#funcion tradicional para escribir en un archivo
        writer.writerow(["id","nombre","precio","stock"])
        
        writer.writerow([1,"Mouse",40,10])
        writer.writerow([1,"Mouse",30,5])
        writer.writerow([1,"Mouse",250,3])
        
def read_inventory() -> None:
    if not FILE_PATH.exists():
        print("El archivo de inventario no existe.")
        return
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("\n *** INVENTARIO ***")
        for row in reader:
            print(row)
            
def read_inventory_formatted() -> None:
    if not FILE_PATH.exists():
        print("El archivo no exite")
        return
    with FILE_PATH.open("r",encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader) # Lee la primera fila como encabezado
        print("-" * 40)
        print("\n *** INVENTARIO CON FORMATO DE SALIDA ***")
        for row in reader:
            print(
                f"ID: {row[0]}"
                f"producto: {row[1]}"
                f"precio: {row[2]}"
                f"stock: {row[3]}"
            )
            
def main() -> None:
    create_inventory_file()
    read_inventory()
    read_inventory_formatted()

if __name__ == "__main__":
    main()