import csv
import json

def leer_csv(ruta):
    datos = []
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def leer_json(ruta):
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        return json.load(archivo)

def calcular_promedios(datos):
    if len(datos) == 0:
        return 0, 0, 0

    suma_edad = 0
    suma_salario = 0
    suma_peso = 0
    cantidad = len(datos)

    for persona in datos:
        suma_edad += float(persona['edad'])
        suma_salario += float(persona['salario'])
        suma_peso += float(persona['peso'])

    return suma_edad/cantidad, suma_salario/cantidad, suma_peso/cantidad