class Carrito:
    """Simula el proceso de compra y validación de stock"""
    def __init__(self):
        self.items = [] #Lista de videojuegos agregados

    def agregar_juego(self, juego):
        """Valida stock disponible antes de agregar"""
        if juego.stock > 0:
            self.items.append(juego)
            juego.stock -= 1 #Reduce el stock en memoria 
            return True
        return False