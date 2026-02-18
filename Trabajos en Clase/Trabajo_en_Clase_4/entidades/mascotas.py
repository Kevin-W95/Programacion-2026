class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f"[Mascota] Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}"