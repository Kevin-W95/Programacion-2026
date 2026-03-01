class CuentaBancaria:
    def __init__(self, numero):
        self.__numero = numero
    def __str__(self):
        return f"Cuenta No: {self.__numero}"

class Persona:
    def __init__(self, nombre, edad, id_cuenta, vehiculo=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__cuenta = CuentaBancaria(id_cuenta)
        self.vehiculo_asignado = vehiculo 

    @property
    def nombre(self): return self.__nombre

    @property
    def edad(self): return self.__edad

    def __str__(self):
        v_info = self.vehiculo_asignado.marca if self.vehiculo_asignado else "Ninguno"
        return (f"Persona: {self.__nombre} | Edad: {self.__edad} | "
                f"{self.__cuenta} | Auto: {v_info}")

    def __len__(self):
        return int(self.__edad)