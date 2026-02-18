class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def __str__(self):
        return f"[Persona] Nombre: {self.nombre}, Edad: {self.edad}, Profesión: {self.profesion}"