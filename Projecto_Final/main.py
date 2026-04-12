from logica.modelos import JuegoPS5, JuegoXbox, JuegoNintendo
from logica.gestionar import cargar_catalogo, guardar_archivo
from logica.tienda import Carrito
import logica.herramientas
import os

def ejecutar():
    print("--- INICIANDO SISTEMA ---")
    catalogo = [] 

    #Inicialización del sistema cargando el catálogo externo
    nombre_archivo = "catalogo.json"

    if not os.path.exists(nombre_archivo):
        nombre_archivo = "catalogo.csv"

    if os.path.exists(nombre_archivo):
        datos_crudos = cargar_catalogo(nombre_archivo)
        print(f"Éxito: Se cargaron {len(datos_crudos)} juegos.")
    else:
        print(f"Error: No se encontró el archivo. Buscando en: {os.path.abspath('data')}")
        datos_crudos = []

    #Aquí iría el bucle para instanciar los juegos
    for d in datos_crudos:  
            if d['consola'] == "PS5":
                catalogo.append(JuegoPS5(d['id'], d['nombre'], d['categoria'], d['precio'], d['esrb'], d['stock']))
            elif d['consola'] == "Xbox":
                catalogo.append(JuegoXbox(d['id'], d['nombre'], d['categoria'], d['precio'], d['esrb'], d['stock']))
            else:
                catalogo.append(JuegoNintendo(d['id'], d['nombre'], d['categoria'], d['precio'], d['esrb'], d['stock']))

    carrito = Carrito()

    while True:
            print("\n--- TIENDA DE VIDEOJUEGOS ---")
            print("1. Ver Catálogo\n2. Agregar Juego\n3. Comprar\n4. Ver Carrito\n5. Finalizar y Salir")
            op = input("Seleccione: ")

            if op == "1":
                print("\n" + "="*70)
                print(f"{'ID':<4} | {'NOMBRE':<35} | {'CONSOLA':<10} | {'PRECIO':<7} | {'STOCK'}")
                print("="*70)
                for juego in catalogo:
                    print(juego)     

            elif op == "2":
                try:
                    #Uso de herramientas para que el código aquí sea de una sola línea
                    id_n = logica.herramientas.validar_id_unico(input("ID: "), catalogo)
                    nom = logica.herramientas.validar_no_vacio(input("Nombre: "), "Nombre")
                    pre = logica.herramientas.leer_numero_positivo("Precio: ")
                    sto = logica.herramientas.leer_numero_positivo("Stock: ", True)
                    
                    print("1. PS5 | 2. Xbox | 3. Nintendo")
                    c = input("Consola: ")
                    if c == "1": n = JuegoPS5(id_n, nom, "General", pre, "T", sto)
                    elif c == "2": n = JuegoXbox(id_n, nom, "General", pre, "T", sto)
                    else: n = JuegoNintendo(id_n, nom, "General", pre, "T", sto)
                    
                    catalogo.append(n)
                    print("¡Agregado!")
                except ValueError as e:
                    print(e)

            elif op == "3":
                id_compra = input("Ingrese ID del juego para comprar: ")
                encontrado = next((j for j in catalogo if str(j._id) == id_compra), None)
                if encontrado and carrito.agregar_juego(encontrado):
                    print(f"Agregado: {encontrado.nombre}")
                else:
                    print("No encontrado o sin stock.")

            elif op == "5":
                #Guardamos cambios en el archivo antes de cerrar
                datos_finales = [j.to_dict() for j in catalogo]
                guardar_archivo("catalogo", datos_finales, "json")
                print("¡Gracias por su visita!")
                break

if __name__ == "__main__":
    ejecutar()