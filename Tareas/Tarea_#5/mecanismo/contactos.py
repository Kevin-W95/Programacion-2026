class Contacto:
    def __init__(self, nombre, telefono, email, edad, residencia):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.edad = int(edad)
        self.residencia = residencia

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "edad": self.edad,
            "residencia": self.residencia
        }

    def __str__(self):
        return f"[{self.nombre}] - Tel: {self.telefono} | Edad: {self.edad} | Ciudad: {self.residencia}"