from logica.modelos import JuegoPS5, JuegoXbox, JuegoNintendo
from logica.gestionar import cargar_catalogo, guardar_archivo
from logica.tienda import Carrito
import logica.herramientas
import os

def ejecutar():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(BASE_DIR, "data", "catalogo.json")
    ruta_csv = os.path.join(BASE_DIR, "data", "catalogo.csv")

    catalogo = [] 
    datos_crudos = []

    #Inicialización del sistema cargando el catálogo externo
    if os.path.exists(ruta_json):
        nombre_archivo = ruta_json
    elif os.path.exists(ruta_csv):
        nombre_archivo = ruta_csv
    else:
        nombre_archivo = None

    if nombre_archivo:
        datos_crudos = cargar_catalogo(nombre_archivo)
        for d in datos_crudos:
            con = str(d.get('consola', '')).upper()
            if "PS5" in con:
                obj = JuegoPS5(d['id'], d['nombre'], d['categoria'], d['precio'], d['esrb'], d['stock'])
            elif "XBOX" in con:
                obj = JuegoXbox(d['id'], d['nombre'], d['categoria'], d['precio'], d['esrb'], d['stock'])
            else:
                obj = JuegoNintendo(d['id'], d['nombre'], d['categoria'], d['precio'], d['esrb'], d['stock'])
            catalogo.append(obj)
        print(f"Sistema iniciado: {len(catalogo)} juegos cargados.")
    else:
        print("Advertencia: No se encontró el catálogo inicial.")

    carrito = Carrito()

    while True:
        print("\n" + "="*30)
        print("   TIENDA DE VIDEOJUEGOS")
        print("="*30)
        print("1. Ver Catálogo")
        print("2. Agregar Juego al Catálogo")
        print("3. Comprar (Añadir al Carrito)")
        print("4. Ver Carrito y Facturar")
        print("5. Salir y Guardar Cambios")
        
        op = input("\nSeleccione una opción: ")

        if op == "1":
            print("\n" + "="*85)
            print(f"{'ID':<4} | {'NOMBRE':<35} | {'CONSOLA':<12} | {'PRECIO':<8} | {'STOCK'}")
            print("="*85)
            for juego in catalogo:
                print(juego)     

        elif op == "2":
            try:
                #Uso de herramientas para que el código aquí sea de una sola línea
                print("\n--- REGISTRAR NUEVO JUEGO ---")
                id_n = logica.herramientas.validar_id_unico(input("ID: "), catalogo)
                name = logica.herramientas.validar_no_vacio(input("Nombre: "), "Nombre")
                price = logica.herramientas.leer_numero_positivo("Precio: ")
                stock = logica.herramientas.leer_numero_positivo("Stock: ", True)
                    
                print("1. PS5 | 2. Xbox | 3. Nintendo")
                c = input("Consola: ")
                if c == "1": n = JuegoPS5(id_n, name, "General", price, "T", stock)
                elif c == "2": n = JuegoXbox(id_n, name, "General", price, "T", stock)
                else: n = JuegoNintendo(id_n, name, "General", price, "T", stock)
                    
                catalogo.append(n)
                print("¡Registrado!")
            except ValueError as e:
                print(f"Error: {e}")

        elif op == "3":
            id_compra = input("Ingrese ID del juego para comprar: ")
            encontrado = next((j for j in catalogo if str(j._id) == id_compra), None)
            if encontrado and encontrado.stock > 0:
                carrito.agregar_juego(encontrado)
                encontrado.stock -= 1
                print(f"{encontrado.nombre} añadido al carrito.")
            else:
                print("No encontrado o sin stock.")

        elif op == "4":
            if not carrito.items:
                print("El carrito está vacío.")
            else:
                print("\n--- FACTURA PROVISIONAL ---")
                for item in carrito.items:
                    print(f"• {item.nombre:<30} ${item.precio:>7}")
                print(f"\nPrecio total de la compra: ${sum(i.precio for i in carrito.items):.2f}")
                
                confirmar = input("\n¿Desea finalizar la compra? (s/n): ")
                if confirmar.lower() == 's':
                    cliente = input("Nombre del cliente: ")
                    #Genera el archivo de factura en la carpeta 'facturas'
                    print(f"Compra finalizada para {cliente}. ¡Gracias!")
                    carrito.items = [] #Limpiar carrito

        elif op == "5":
            #Guardamos cambios en el archivo antes de cerrar
            datos_finales = []
            for j in catalogo:
                datos_finales.append({
                    "id": j.id, "nombre": j.nombre, "categoria": j.categoria,
                    "precio": j.precio, "esrb": j.esrb, "stock": j.stock, "consola": j.consola
                })
            
            #Guardamos en la misma ruta que abrimos
            ruta_guardado = ruta_json if ruta_json else os.path.join(BASE_DIR, "data", "catalogo.json")
            guardar_archivo(ruta_guardado, datos_finales)
            print("Cambios guardados. ¡Hasta luego!")
            break

if __name__ == "__main__":
    ejecutar()