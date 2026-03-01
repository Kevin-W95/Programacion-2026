class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self): return self.__marca

    @property
    def modelo(self): return self.__modelo

    def __str__(self):
        return f"Vehículo: {self.__marca} {self.__modelo}"

    def __len__(self):
        # Retorna el año del modelo (suponiendo que es numérico)
        return int(self.__modelo) if self.__modelo.isdigit() else 0