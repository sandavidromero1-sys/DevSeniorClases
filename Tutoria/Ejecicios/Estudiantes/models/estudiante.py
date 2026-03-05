class Estudiante:
    def __init__(self,id,nombre,edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
    
    def to_list(self):
        return [self.id,self.nombre,self.edad]