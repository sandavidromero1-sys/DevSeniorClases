from abc import ABC, abstractmethod
#abstract base clase
class MonstroBase(ABC):
    @abstractmethod
    def gritoGuerra(self):
        pass
class MounstroGriton(MonstroBase):
    def gritoGuerra(self):
        return "!!ARRRRRRRRRRGGGGGGGGGGGGGGGGGGGGGGGG!!"
    
marian = MounstroGriton()
print(marian.gritoGuerra())
        
class Comportamientos(ABC):
    
    @abstractmethod
    def atacar (self):
        pass
    @abstractmethod
    def defender(self):
        pass

class MonstruoGuerrero(Comportamientos):
     
    def atacar (self):
        return "El mounstro ataca con fuerza"
    @abstractmethod
    def defender(self):
        return "El mosunstro se defiende con un escudo"
   