import json
import csv

def leer_json(ruta):
    try:
        archivo = open(ruta, 'r', encoding='utf-8')
        datos = json.load(archivo)
        archivo.close()
        return datos
    except:
        return []

def guardar_json(ruta, lista_objetos):
    lista_nueva = []
    for contacto in lista_objetos:
        diccionario = contacto.to_dict()
        lista_nueva.append(diccionario)

    archivo = open(ruta, 'w', encoding='utf-8')
    json.dump(lista_nueva, archivo, indent=4)
    archivo.close()

def leer_csv(ruta):
    lista_de_contactos = []
    try:
        archivo = open(ruta, 'r', encoding='utf-8')
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista_de_contactos.append(fila)
        archivo.close()
        return lista_de_contactos
    except:
        return []

def guardar_csv(ruta, lista_objetos):
    if len(lista_objetos) == 0:
        return

    columnas = ["nombre", "telefono", "email", "edad", "residencia"]
    
    archivo = open(ruta, 'w', newline='', encoding='utf-8')
    escritor = csv.DictWriter(archivo, fieldnames=columnas)

    escritor.writeheader()

    for contacto in lista_objetos:
        datos_fila = contacto.to_dict()
        escritor.writerow(datos_fila)
        
    archivo.close()