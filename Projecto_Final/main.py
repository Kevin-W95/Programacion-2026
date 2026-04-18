from logica.modelos import JuegoPS5, JuegoXbox, JuegoNintendo
from logica.gestionar import cargar_catalogo, guardar_archivo
from logica.tienda import Carrito
import logica.herramientas
import os
import json
import csv
from datetime import datetime

def escribir_factura_txt(ruta, cliente, items, total):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"Factura de Venta\nFecha: {datetime.now().strftime('%Y-%m-%d')}\nCliente: {cliente}\n" + "="*30 + "\n")
        for i in items:
            f.write(f"{i.nombre:<20} ${i.precio:>7.2f}\n")
        f.write("="*35 + f"\nTOTAL A PAGAR: ${total:.2f}")


def escribir_factura_json(ruta, cliente, items, total):
    factura = {
        "Factura": {
            "Fecha": datetime.now().strftime("%Y-%m-%d"),
            "Cliente": cliente,
            "Detalle": [{"Nombre": i.nombre, "Precio": i.precio} for i in items],
            "Total": total
        }
    }
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(factura, f, indent=2, ensure_ascii=False)


def escribir_factura_csv(ruta, cliente, items, total):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Factura de Venta"])
        writer.writerow(["Fecha", datetime.now().strftime("%Y-%m-%d")])
        writer.writerow(["Cliente", cliente])
        writer.writerow([])
        writer.writerow(["Nombre", "Precio"])
        for i in items:
            writer.writerow([i.nombre, f"{i.precio:.2f}"])
        writer.writerow([])
        writer.writerow(["TOTAL A PAGAR", f"{total:.2f}"])


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
        print(f"Cargando catálogo desde: {nombre_archivo}")
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
        print("4. Ver Carrito, Eliminar o Facturar")
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
                print(f"{encontrado.nombre} añadido al carrito.")
            else:
                print("No encontrado o sin stock.")

        elif op == "4":
            if not carrito.items:
                print("El carrito está vacío.")
            else:
                while True:
                    total_compra = sum(i.precio for i in carrito.items)
                    print("\n--- FACTURA PROVISIONAL ---")
                    for item in carrito.items:
                        print(f"• {item.nombre:<30} ${item.precio:>7}")
                    print(f"\nPrecio total de la compra: ${total_compra:.2f}")

                    print("\nOpciones:")
                    print("1. Eliminar juego del carrito")
                    print("2. Finalizar compra")
                    print("3. Volver al menú")
                    sub_op = input("Seleccione una opción: ").strip()

                    if sub_op == "1":
                        id_eliminar = input("Ingrese ID o nombre del juego a eliminar: ").strip()
                        encontrado_carrito = next((j for j in carrito.items if str(j._id) == id_eliminar or j.nombre.lower() == id_eliminar.lower()), None)
                        if encontrado_carrito:
                            carrito.items.remove(encontrado_carrito)
                            encontrado_carrito.stock += 1
                            print(f"{encontrado_carrito.nombre} eliminado del carrito.")
                            if not carrito.items:
                                print("El carrito está vacío.")
                                break
                        else:
                            print("No se encontró ese juego en el carrito.")
                    elif sub_op == "2":
                        cliente = input("Nombre del cliente: ")

                        folder_facturas = os.path.join(BASE_DIR, "data", "facturas")
                        os.makedirs(folder_facturas, exist_ok=True)

                        print("\nSeleccione el formato de factura:")
                        print("1. TXT")
                        print("2. JSON")
                        print("3. CSV")
                        formato = input("Opción: ").strip()
                        if formato == "2":
                            extension = "json"
                        elif formato == "3":
                            extension = "csv"
                        else:
                            extension = "txt"

                        nombre_factura = f"{cliente.replace(' ', '_')}.{extension}"
                        ruta_factura = os.path.join(folder_facturas, nombre_factura)

                        if extension == "json":
                            escribir_factura_json(ruta_factura, cliente, carrito.items, total_compra)
                        elif extension == "csv":
                            escribir_factura_csv(ruta_factura, cliente, carrito.items, total_compra)
                        else:
                            escribir_factura_txt(ruta_factura, cliente, carrito.items, total_compra)

                        print(f"Factura creada: {ruta_factura}")
                        print(f"Compra finalizada para {cliente}. ¡Gracias!")
                        carrito.items = []
                        break
                    else:
                        break

        elif op == "5":
            #Se guardan los cambios en el archivo antes de cerrar
            datos_finales = []
            for j in catalogo:
                datos_finales.append({
                    "id": j.id, "nombre": j.nombre, "categoria": j.categoria,
                    "precio": j.precio, "esrb": j.esrb, "stock": j.stock, "consola": j.consola
                })
            
            #Se guarda en la misma ruta 
            ruta_guardado = nombre_archivo if nombre_archivo else os.path.join(BASE_DIR, "data", "catalogo.json")
            guardar_archivo(ruta_guardado, datos_finales)
            print("Cambios guardados. ¡Hasta luego!")
            break

if __name__ == "__main__":
    ejecutar()