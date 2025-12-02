class Avion:
    def _init_(self, motor, marca, tipo, capacidad):
        self.motor = motor
        self.marca = marca
        self.tipo  = tipo
        self.capacidad = capacidad
    
    def _str_(self):
        return f"Avion(motor={self.motor}, marca={self.marca}, tipo={self.tipo}, capacidad={self.capacidad})"
    
        
    
class Carro:    
    def _init_(self, modelo,cilindraje,capcidadpasajeros,marca):
        self.modelo = modelo 
        self.cilindraje = cilindraje
        self.capcidadpasajeros = capcidadpasajeros
        self.marca = marca

class Cliente:
    def _init_(self, documento,nombre,apellidos,ciudad):
        self.documento = documento
        self.nombre = nombre
        self.apellidos = apellidos  
        self.ciudad = ciudad   

avion1=Avion("Rolls-Royce Trent 1000","Boeing","Comercial",300)
avion2 = Avion("CFM56-3B","Tucano","Combate","2")
avion3 = Avion("TPE331","Gavilan","Avioneta","6")

print(avion1)