from Figura import *
from Color import *

class Cuadrado(Figura,Color):
    def __init__(self, color, lado):
        Figura.__init__(self,lado,lado)
        Color.__init__(self,color)

    def __str__(self) -> str:
        return f"{Figura.__str__(self)} {Color.__str__(self)} Area: {self.CalcularArea()}"

    def CalcularArea(self):
        return self._lado * self._ancho


Cuadrado1 = Cuadrado("rojo",5)
print(Cuadrado1.CalcularArea())
