class Animal:
    """Clase base para todos los animales del zoológico."""
    def __init__(self, nombre_individual, edad):
        self._nombre_individual = nombre_individual
        self._edad = edad

    @property
    def nombre_individual(self):
        return self._nombre_individual

    def __str__(self):
        return f"Nombre: {self._nombre_individual}, Edad: {self._edad}"

class Pez(Animal):
    def __str__(self):
        return f"Tipo: Pez | {super().__str__()}"

class Tiburon(Pez):
    def __str__(self):
        return f"Especie: Tiburón | {super().__str__()}"

class Mamifero(Animal):
    def __str__(self): return f"Tipo: Mamífero | {super().__str__()}"

class Leon(Mamifero):
    def __str__(self): return f"Especie: León | {super().__str__()}"