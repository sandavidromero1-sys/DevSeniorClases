class Mounstro():
    def __init__(self, nombre,color,poder):
        self.nombre = nombre
        self.color = color 
        self.poder = poder
    
    def asustar(self):
        return f"{self.nombre} esta sustando con su poder de {self.poder}"
class MounstroEmpanador(Mounstro):
    def atacar(self):
        return f"{self.nombre} esta empanando todo lo que encuentra"
class MousntroBostezador (Mounstro):
    def atacar(self):
        return f"{self.nombre} estado bostezando y contagiando el bostezo"
    def asustar(self):
        return super().asustar()
ejercitoMounstros=[MousntroBostezador("juanes","azul","bostezar fuerte"),MounstroEmpanador("alexito","amarillo","hacer empanadas")]
for mounstro in ejercitoMounstros:
    print(mounstro.atacar())
class MousntroJefe():
    def __init__(self, nombre, color, poder, vida):
        self.nombre = nombre
        self.color = color
        self.poder = poder
        self._vida = 100
    def recibirGolpes(self):
        self._vida -= 10
        return f"{self.nombre} tiene {self._vida} de vida"
    
jefe = MousntroJefe ("Dracula", "rojo" , "chaupar sangre", 100)
print(jefe.recibirGolpes())
        
       