import json
import csv
import os

"""Carga datos desde archivos externos manejando excepciones"""
def cargar_catalogo(ruta):
    try:
        if not os.path.exists(ruta): return []
        #Sirve para leer el archivo JSON
        if ruta.endswith('.json'):
            with open(ruta, 'r') as f:
                return json.load(f)
        #Es para leer el archivo CSV
        elif ruta.endswith('.csv'):
            with open(ruta, 'r') as f:
                return list(csv.DictReader(f))
    except Exception as e:
        print(f"Error al cargar archivo: {e}")
        return []

"""Guarda facturas o el catálogo actualizado en el formato elegido por el usuario"""
def guardar_archivo(ruta, datos, formato):
    try:
        if formato.lower() == 'json':
            with open(f"{ruta}.json", 'w') as f:
                json.dump(datos, f, indent=4)
        elif formato.lower() == 'csv':
            if not datos: return
            with open(f"{ruta}.csv", 'w', newline='') as f:
                #Usa la primera fila para definir los encabezados del CSV
                writer = csv.DictWriter(f, fieldnames=datos[0].keys())
                writer.writeheader()
                writer.writerows(datos)
        print(f"Archivo {ruta}.{formato} guardado exitosamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")