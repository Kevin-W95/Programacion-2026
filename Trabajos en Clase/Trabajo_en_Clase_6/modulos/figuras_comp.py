import math
from .Abstract import Figura

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio, self.altura = radio, altura
    def volumen(self):
        return math.pi * (self.radio ** 2) * self.altura
    
class Cono(Figura):
    def __init__(self, radio, altura):
        self.radio, self.altura = radio, altura
    def volumen(self):
        return (1/3) * math.pi * (self.radio ** 2) * self.altura
    
class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado
    def volumen(self):
        return self.lado ** 3
    
class Esfera(Figura):
    def __init__(self, radio):
        self.radio = radio
    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)
    
class Paralelepipedo(Figura):
    def __init__(self, largo, ancho, alto):
        self.largo, self.ancho, self.alto = largo, ancho, alto
    def volumen(self):
        return self.largo * self.ancho * self.alto