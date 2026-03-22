from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def volumen(self):
        """Método abstracto que obliga a las hijas a calcular su volumen"""
        pass