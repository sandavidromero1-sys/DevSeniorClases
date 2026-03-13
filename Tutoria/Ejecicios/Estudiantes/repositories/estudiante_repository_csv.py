import csv
import os
from models.estudiante import Estudiante
from repositories.base_repository import BaseRepository

class EstudianteRepositoryCSV(BaseRepository):
    def __init__(self, archivo="data/estudiantes.csv", archivo_txt="data/lista_supermercado.txt"):
        self.archivo = archivo
        self.archivo_txt = archivo_txt

        # Verificar si la carpeta 'data' existe, y si no, crearla
        if not os.path.exists(os.path.dirname(self.archivo)):
            os.makedirs(os.path.dirname(self.archivo))  # Crea la carpeta 'data' si no existe

        # Verificar si el archivo existe, si no, crear el archivo con la cabecera correcta
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w', newline='') as f:
                writer = csv.writer(f)
                # Escribe la cabecera solo si el archivo no existe
                writer.writerow(['id', 'nombre', 'edad'])
    
    def _leer_archivo(self):
        with open(self.archivo, 'r', newline='') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]  # Aquí se leen solo los datos
            return data

    def _guardar_archivo(self, data):
        # Solo agregar datos al archivo (sin sobrescribir el encabezado)
        with open(self.archivo, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)  # Solo guarda los datos sin el encabezado

    def agregar(self, estudiante: Estudiante):
        # Leer los datos actuales en el archivo
        data = self._leer_archivo()
        # Convertimos el estudiante a una lista (sin apellido)
        data.append(estudiante.to_list())
        # Guardar los datos sin el encabezado
        self._guardar_archivo(data)

    def obtener_por_id(self, id):
        data = self._leer_archivo()
        for est in data:
            if int(est['id']) == id:  # Acceso por 'id' como clave de diccionario
                return Estudiante.from_list(est)
        return None

    def listar(self):
        data = self._leer_archivo()
        # Retornamos los estudiantes como objetos Estudiante
        return [Estudiante.from_list(est) for est in data]

    def eliminar(self, id):
        data = self._leer_archivo()
        data = [est for est in data if int(est['id']) != id]  # Acceso por 'id' como clave de diccionario
        self._guardar_archivo(data)
        return True

    # Función para generar el archivo .txt como lista de supermercado
    def generar_lista_supermercado_txt(self):
        estudiantes = self.listar()
        
        with open(self.archivo_txt, 'w') as f:
            f.write("Lista de Estudiantes - Supermercado\n")
            f.write("=" * 40 + "\n")
            for estudiante in estudiantes:
                f.write(f"ID: {estudiante.id} - Nombre: {estudiante.nombre} - Edad: {estudiante.edad} años\n")
            f.write("=" * 40 + "\n")
            f.write("¡Fin de la lista!\n")

        print(f"El archivo de lista de supermercado ha sido generado en: {self.archivo_txt}")