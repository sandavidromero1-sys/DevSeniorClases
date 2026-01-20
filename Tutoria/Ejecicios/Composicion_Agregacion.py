class Salario:
    def __init__(self,monto,bono):
        self.monto = monto
        self.bono = bono
        
    def salario_anual(self):
        return(self.monto * 12) + self.bono
    
class Empleado:
    def __init__(self,nombre,puesto,salario):
        self.nombre = nombre
        self.puesto = puesto
        
        self.agg_salario = salario
        
    def total(self):
        return self.agg_salario.salario_anual()
    
salario = Salario(3000, 5000)

empleado = Empleado("Juan","Inge", salario)

print(empleado.total())