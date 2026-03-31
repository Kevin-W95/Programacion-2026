import json
import csv

agenda = []
archivo_actual = ""
tipo_archivo = ""

def cargar_archivo():
    global agenda, archivo_actual, tipo_archivo
    print("1. JSON")
    print("2. CSV")
    op = input("Seleccione tipo: ")
    nombre = input("Nombre del archivo: ")
    
    if op == "1":
        archivo = open(nombre, "r")
        agenda = json.load(archivo)
        archivo.close()
        tipo_archivo = "json"
    else:
        archivo = open(nombre, "r")
        lector = csv.DictReader(archivo)
        agenda = list(lector)
        archivo.close()
        tipo_archivo = "csv"
    
    archivo_actual = nombre
    print("¡Archivo cargado!")

def agregar_contacto():
    if archivo_actual == "":
        print("Carga un archivo primero")
        return

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    tel = input("Tel: ")
    email = input("Email: ")
    res = input("Ciudad: ")

    nuevo = {
        "nombre": nombre,
        "edad": edad,
        "telefono": tel,
        "email": email,
        "residencia": res
    }
    
    agenda.append(nuevo)

    if tipo_archivo == "json":
        f = open(archivo_actual, "w")
        json.dump(agenda, f, indent=4)
        f.close()
    else:
        f = open(archivo_actual, "w", newline="")
        columnas = ["nombre", "edad", "telefono", "email", "residencia"]
        escritor = csv.DictWriter(f, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(agenda)
        f.close()
    print("Guardado.")

def buscar_nombre():
    buscar = input("Nombre a buscar: ").lower()
    for persona in agenda:
        if buscar in persona["nombre"].lower():
            print("Encontrado:", persona["nombre"], "-", persona["telefono"])

while True:
    print("\n--- MI AGENDA ---")
    print("1. Cargar")
    print("2. Agregar")
    print("3. Buscar")
    print("4. Salir")
    
    opcion = input("Elija: ")
    
    if opcion == "1":
        cargar_archivo()
    elif opcion == "2":
        agregar_contacto()
    elif opcion == "3":
        buscar_nombre()
    elif opcion == "4":
        break