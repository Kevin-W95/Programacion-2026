class Empleado:
    """Clase padre para representar a cualquier trabajador del zoológico."""
    def __init__(self, nombre, id_empleado):
        self._nombre = nombre
        self._id_empleado = id_empleado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    def __str__(self):
        return f"Empleado: {self._nombre} | ID: {self._id_empleado}"

class Administrador(Empleado):
    def __str__(self):
        return f"[Administrador] {super().__str__()}"

class Guardian(Empleado):
    def __str__(self):
        return f"[Guardián] {super().__str__()}"

class Conserje(Empleado):
    def __str__(self):
        return f"[Conserje] {super().__str__()}"

class Veterinario(Empleado):
    def __str__(self):
        return f"[Veterinario] {super().__str__()}"