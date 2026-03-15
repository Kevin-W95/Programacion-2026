class Transporte:
    """Clase base para los medios de locomoción en el zoológico."""
    def __init__(self, codigo):
        self._codigo = codigo

    @property
    def codigo(self):
        return self._codigo

    def __str__(self):
        return f"ID Transporte: {self._codigo}"

class Bicicleta(Transporte):
    def __str__(self): return f"Bicicleta - {super().__str__()}"

class Cuadraciclo(Transporte):
    def __str__(self): return f"Cuadraciclo - {super().__str__()}"

class Patineta(Transporte):
    def __str__(self): return f"Patineta - {super().__str__()}"