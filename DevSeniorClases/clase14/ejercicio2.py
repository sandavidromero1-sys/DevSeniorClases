from abc import ABC, abstractmethod
#Interfaz para reportes
class GenerarReporte(ABC):
    @abstractmethod
    def generar_reporte(self)->None:
        pass
class SistemaPago(ABC):
    def __init__(self,monto:float)->None:
        self.monto = monto
    
    @abstractmethod
    def procesar_pago(self) -> None:
        