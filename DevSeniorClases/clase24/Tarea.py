import csv
from pathlib import Path

FILE_PATH = Path("registro_avistamientos.csv")

def create_registro_file()-> None:
    fieldnames = ["avistamiento_id","especie","zona","cantidad"]
    
    with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader()
        
        write.writerow(
            {       
            "avistamiento_id":1,
            "especie":"Condor",
            "zona":"Montaña",
            "cantidad":5
            }
            )
        
        write.writerow(
            {
            "avistamiento_id":2,
            "especie":"Jaguar",
            "zona":"Selva",
            "cantidad":3 
             }
            )
        
        write.writerow(
            {
            "avistamiento_id":3,
            "especie":"conejo",
            "zona":"Zona Norte",
            "cantidad":20
             }
            )
        write.writerow(
            {
            "avistamiento_id":4,
            "especie":"Pajaro",
            "zona":"Bosque",
            "cantidad":15
            }
            )
        write.writerow(
            {
            "avistamiento_id":5,
            "especie":"Serpiente",
            "zona":"Zona Sur",
            "cantidad":50
            }
        )
        write.writerow(
            {
            "avistamiento_id":6,
            "especie":"Tortuga",
            "zona":"Río",
            "cantidad":10
            }
        )
        write.writerow(
            {
            "avistamiento_id":7,
            "especie":"Mono",
            "zona":"Selva",
            "cantidad":8
            }
        )
        write.writerow(
            {
                "avistamiento_id":8,
                "especie":"Zorro",
                "zona":"Zona Norte",
                "cantidad":12
            }
        )
        write.writerow(
            {
                "avistamiento_id":9,
                "especie":"Oso",
                "zona":"Montaña",
                "cantidad":4
            }
        )
        write.writerow(
            {
                "avistamiento_id":10,
                "especie":"Puma",
                "zona":"Zona Sur",
                "cantidad":6
            }
        )
        
        
def leer_datos_crudos() -> None:
    if not FILE_PATH.exists():
        print("El archivo no existe.")
        return
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\n*** VISTA  DE DEPURACION ***\n")
        for row in reader:
            print(row)
def mostrar_reporte_biologico() -> None:
    if not FILE_PATH.exists():
        print("El archivo no existe.")
        return
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\n*** VISTA REPORTE ***\n")
        for row in reader:
            print(f"[{row['avistamiento_id']}] "
                f"Especie: {row['especie']} | "
                f"Localización: {row['zona']} | "
                f"Ejemplares: {row['cantidad']}.")
            
def main() -> None:
    if not FILE_PATH.exists():
        create_registro_file()
    leer_datos_crudos()
    mostrar_reporte_biologico()
        
if __name__ == "__main__":
    main()
        
        
        
        
        