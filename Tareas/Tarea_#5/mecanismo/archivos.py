import json
import csv

def leer_json(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_json(ruta, lista_objetos):
    with open(ruta, 'w', encoding='utf-8') as f:
        # Convertimos cada objeto Contacto a diccionario antes de guardar
        datos = [c.to_dict() for c in lista_objetos]
        json.dump(datos, f, indent=4)

def leer_csv(ruta):
    contactos = []
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                contactos.append(fila)
        return contactos
    except FileNotFoundError:
        return []

def guardar_csv(ruta, lista_objetos):
    if not lista_objetos: return
    columnas = ["nombre", "telefono", "email", "edad", "residencia"]
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=columnas)
        escritor.writeheader()
        for c in lista_objetos:
            escritor.writerow(c.to_dict())