class Mascota:
    def __init__(self, nombre, especie, edad):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad

    @property
    def nombre(self): return self.__nombre
    
    @nombre.setter
    def nombre(self, valor): self.__nombre = valor

    @property
    def especie(self): return self.__especie

    @property
    def edad(self): return self.__edad

    def __str__(self):
        return f"Mascota: {self.__nombre} ({self.__especie}), {self.__edad} años"

    def __len__(self):
        return len(self.__nombre)