class Estudiante:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
    
    def to_list(self):
        return [self.id, self.nombre, self.edad]
    
    @staticmethod
    def from_list(data):
        # Acceder usando las claves del diccionario
        return Estudiante(int(data['id']), data['nombre'], int(data['edad']))  # Correcto, usa claves