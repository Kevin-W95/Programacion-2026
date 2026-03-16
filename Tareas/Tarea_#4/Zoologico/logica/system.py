from entidades.workers import Administrador, Guardian, Conserje, Veterinario
from entidades.transport import Bicicleta, Cuadraciclo, Patineta
from entidades.animal import Leon, Tiburon, Serpiente, Loro, Rana

# Listas donde se guardarán los objetos 
lista_empleados = []
lista_transportes = []
lista_animales = []

def registrar_empleado(tipo, nombre, id_emp):
    """Crea el objeto según el tipo y lo guarda en la lista."""
    if tipo == "1": nuevo = Administrador(nombre, id_emp)
    elif tipo == "2": nuevo = Guardian(nombre, id_emp)
    elif tipo == "3": nuevo = Conserje(nombre, id_emp)
    elif tipo == "4": nuevo = Veterinario(nombre, id_emp)
    else: return
    lista_empleados.append(nuevo)

def registrar_animal(tipo, nombre, edad):
    """Crea la especie específica según la categoría elegida."""
    # Categorías a las clases hijas específicas
    if tipo == "1": nuevo = Serpiente(nombre, edad)
    elif tipo == "2": nuevo = Leon(nombre, edad)
    elif tipo == "3": nuevo = Loro(nombre, edad)
    elif tipo == "4": nuevo = Tiburon(nombre, edad)
    elif tipo == "5": nuevo = Rana(nombre, edad)
    else: return
    lista_animales.append(nuevo)

def registrar_transporte(tipo, codigo):
    """Crea el objeto de transporte y lo guarda en la lista."""
    if tipo == "1": nuevo = Bicicleta(codigo)
    elif tipo == "2": nuevo = Cuadraciclo(codigo)
    elif tipo == "3": nuevo = Patineta(codigo)
    else: return
    lista_transportes.append(nuevo)

def listar_todo(lista):
    """Recorre cualquier lista e imprime los objetos usando su método __str__"""
    if not lista:
        print("No hay registros guardados.")
    else:
        for item in lista:
            print(item)