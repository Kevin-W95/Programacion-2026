class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"[Vehículo] Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"