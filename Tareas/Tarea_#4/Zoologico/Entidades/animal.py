class Animal:
    """
    Clase base que define las características generales de cualquier animal del zoológico.
    """
    def __init__(self, nombre_individual, edad):
        # Atributos privados
        self._nombre_individual = nombre_individual
        self._edad = edad

    @property
    def nombre_individual(self):
        return self._nombre_individual

    @nombre_individual.setter
    def nombre_individual(self, valor):
        self._nombre_individual = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self._edad = valor

    def __str__(self):
        return f"Nombre: {self._nombre_individual} | Edad: {self._edad} años"

# Categorías

class Reptil(Animal):
    def __str__(self):
        return f"[REPTIL] {super().__str__()}"

class Mamifero(Animal):
    def __str__(self):
        return f"[MAMÍFERO] {super().__str__()}"

class Ave(Animal):
    def __str__(self):
        return f"[AVE] {super().__str__()}"

class Pez(Animal):
    def __str__(self):
        return f"[PEZ] {super().__str__()}"

class Anfibio(Animal):
    def __str__(self):
        return f"[ANFIBIO] {super().__str__()}"

# Especies específicas

class Serpiente(Reptil):
    def __str__(self):
        return f"Especie: Serpiente | {super().__str__()}"

class Leon(Mamifero):
    def __str__(self):
        return f"Especie: León | {super().__str__()}"

class Loro(Ave):
    def __str__(self):
        return f"Especie: Loro | {super().__str__()}"

class Tiburon(Pez):
    def __str__(self):
        return f"Especie: Tiburón | {super().__str__()}"

class Rana(Anfibio):
    def __str__(self):
        return f"Especie: Rana | {super().__str__()}"