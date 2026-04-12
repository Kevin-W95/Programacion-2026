class VideoJuego:
    """Clase padre que define los atributos base de cualquier videojuego."""
    def __init__(self, id_unico, nombre, categoria, precio, esrb, stock, consola):
        #Atributos protegidos
        self._id = id_unico 
        self.nombre = nombre
        self.categoria = categoria
        self._precio = float(precio)
        self.esrb = esrb
        self._stock = int(stock)
        self.consola = consola

    #Decorador para leer el precio y stock de forma segura
    @property 
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    #Valida que el stock no sea negativo al modificarlo
    @stock.setter
    def stock(self, valor):
        if valor >= 0:
            self._stock = valor
        else:
            raise ValueError("No se permite stock negativo")

    def to_dict(self):
        return {
            "id": self._id, "nombre": self.nombre, "categoria": self.categoria,
            "precio": self._precio, "esrb": self.esrb, "stock": self._stock, "consola": self.consola
        }

    def __str__(self):
        return f"ID: {self._id:<3} | {self.nombre:<35} | {self.consola:<10} | ${self.precio:>6} | Stock: {self.stock}"
    
#Herencia: Clases hijas 
class JuegoPS5(VideoJuego):
    def __init__(self, id_u, nom, cat, pre, esrb, sto):
        super().__init__(id_u, nom, cat, pre, esrb, sto, "PS5")

class JuegoXbox(VideoJuego):
    def __init__(self, id_u, nom, cat, pre, esrb, sto):
        super().__init__(id_u, nom, cat, pre, esrb, sto, "Xbox")

class JuegoNintendo(VideoJuego):
    def __init__(self, id_u, nom, cat, pre, esrb, sto):
        super().__init__(id_u, nom, cat, pre, esrb, sto, "Nintendo Switch")