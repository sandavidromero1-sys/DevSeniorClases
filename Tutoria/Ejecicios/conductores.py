

class Carro:
    def __init__(self,motor,conductor):
        self.motor = motor
        self.agg_conductor = conductor
class Moto:
    def __init__(self,motor,conductor):
        self.motor = motor
        self.agg_conductor = conductor
class Camion:
    def __init__(self,motor,conductor):
        self.motor = motor
        self.agg_conductor = conductor
class conductor:
    def __init__(self, nombre, edad,licencia,telefono):
        self.nombre = nombre
        self.edad = edad
        self.licencia = licencia
        self.telefono = telefono

conductor1 = conductor("Juan", 30, "A12345", "555-1234")
conductor2 = conductor("Maria", 28, "B67890", "555-5678")
conductor3 = conductor("Carlos", 35, "C54321", "555-8765")

moto1 = Moto("MotorX", conductor1)
carro1 = Carro("MotorY", conductor2)
camion1 = Camion("MotorZ", conductor3)

print("Conductor de la moto:", moto1.agg_conductor.nombre)
print("Conductor del carro:", carro1.agg_conductor.nombre)
print("Conductor del camion:", camion1.agg_conductor.nombre)