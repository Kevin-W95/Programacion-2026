from Entidades.workers import Administrador, Guardian, Conserje, Veterinario
from Entidades.transport import Bicicleta, Cuadraciclo, Patineta
from Entidades.animal import Leon, Tiburon

lista_empleados = []
lista_transportes = []
lista_animales = []

def registrar_empleado(tipo, nombre, id_emp):
    """Crea el objeto según el tipo y lo guarda en la lista."""
    if tipo == "1":
        nuevo = Administrador(nombre, id_emp)
    elif tipo == "2":
        nuevo = Guardian(nombre, id_emp) 
    elif tipo == "3":
        nuevo = Conserje(nombre, id_emp)
    elif tipo == "4":
        nuevo = Veterinario(nombre, id_emp) 
    
    lista_empleados.append(nuevo)

def listar_todo(lista):
    """Recorre cualquier lista e imprime los objetos usando su método __str__."""
    if not lista:
        print("No hay registros guardados.")
    for item in lista:
        print(item)