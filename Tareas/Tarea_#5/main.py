# main.py
from mecanismo.contactos import Contacto
from mecanismo import archivos as gestor

class AgendaHolmes:
    def __init__(self):
        self.lista_contactos = []
        self.archivo_actual = None
        self.formato_actual = None # 'json' o 'csv'

    def ejecutar(self):
        while True:
            print("\n--- AGENDA DE SHERLOCK HOLMES ---")
            print("1. Cargar archivo (JSON/CSV)")
            print("2. Agregar contacto")
            print("3. Buscar por nombre (parcial)")
            print("4. Buscar por teléfono (parcial)")
            print("5. Mostrar promedio de edad")
            print("6. Mostrar todos")
            print("7. Salir")
            
            op = input("Seleccione: ")
            if op == "1": self.menu_cargar()
            elif op == "2": self.menu_agregar()
            elif op == "3": self.buscar_nombre()
            elif op == "4": self.buscar_telefono()
            elif op == "5": self.promedio_edad()
            elif op == "6": self.mostrar_todos()
            elif op == "7": break

    def menu_cargar(self):
        tipo = input("¿Tipo de archivo? (1. JSON / 2. CSV): ")
        ruta = input("Nombre del archivo (ej: personas.json): ")
        
        if tipo == "1":
            datos = gestor.leer_json(ruta)
            self.formato_actual = "json"
        else:
            datos = gestor.leer_csv(ruta)
            self.formato_actual = "csv"
            
        self.archivo_actual = ruta
        # Transformar diccionarios en objetos Contacto
        self.lista_contactos = []
        for d in datos:
            # Creamos el objeto asegurándonos de que tenga los campos del PDF
            c = Contacto(
                d.get('nombre','?'), d.get('telefono','?'), 
                d.get('email','?'), d.get('edad',0), d.get('residencia','?')
            )
            self.lista_contactos.append(c)
        print(f"Cargados {len(self.lista_contactos)} contactos.")

    def menu_agregar(self):
        if not self.archivo_actual:
            print("Error: Primero cargue un archivo.")
            return
        
        nuevo = Contacto(
            input("Nombre: "), input("Teléfono: "),
            input("Email: "), input("Edad: "), input("Residencia: ")
        )
        self.lista_contactos.append(nuevo)
        
        # Guardar inmediatamente
        if self.formato_actual == "json":
            gestor.guardar_json(self.archivo_actual, self.lista_contactos)
        else:
            gestor.guardar_csv(self.archivo_actual, self.lista_contactos)
        print("Guardado con éxito.")

    def buscar_nombre(self):
        termino = input("Nombre a buscar: ").lower()
        encontrados = [c for c in self.lista_contactos if termino in c.nombre.lower()]
        for e in encontrados: print(e)

    def buscar_telefono(self):
        termino = input("Teléfono a buscar: ")
        encontrados = [c for c in self.lista_contactos if termino in c.telefono]
        for e in encontrados: print(e)

    def promedio_edad(self):
        if not self.lista_contactos: return
        total = sum(c.edad for c in self.lista_contactos)
        print(f"Promedio de edad: {total / len(self.lista_contactos):.2f}")

    def mostrar_todos(self):
        for c in self.lista_contactos:
            print(c)

if __name__ == "__main__":
    app = AgendaHolmes()
    app.ejecutar()