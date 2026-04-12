from datetime import datetime

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

    def generar_datos_factura(self, nombre_cliente):
        """Estructura la información requerida para la factura final"""
        total = sum(item.precio for item in self.items)
        return {
            "Cliente": nombre_cliente,
            "Fecha": datetime.now().strftime("%Y-%m-%d"), 
            "Detalle": [{"Nombre": i.nombre, "Precio": i.precio} for i in self.items], 
            "Total": total 
        }