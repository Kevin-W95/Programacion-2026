import json
import csv
import os

"""Carga datos desde archivos externos manejando excepciones"""
def cargar_catalogo(ruta):
    if not os.path.exists(ruta):
        print(f"Archivo no encontrado: {ruta}")
        return []

    try:
        if ruta.lower().endswith('.json'):
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif ruta.lower().endswith('.csv'):
            with open(ruta, 'r', encoding='utf-8', newline='') as f:
                return list(csv.DictReader(f))
        else:
            print(f"Formato no soportado para cargar: {ruta}")
            return []
    except json.JSONDecodeError as e:
        print(f"Error de JSON en {ruta}: {e}")
    except csv.Error as e:
        print(f"Error de CSV en {ruta}: {e}")
    except Exception as e:
        print(f"Error al cargar archivo {ruta}: {e}")
    return []

"""Guarda facturas o el catálogo actualizado en el formato elegido por el usuario"""
def guardar_archivo(ruta, datos, formato=None):
    try:
        if formato:
            formato = formato.lower()
        else:
            _, ext = os.path.splitext(ruta)
            formato = ext[1:].lower() if ext else 'json'

        if formato == 'json':
            file_path = ruta if ruta.lower().endswith('.json') else f"{ruta}.json"
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
        elif formato == 'csv':
            if not datos:
                return
            file_path = ruta if ruta.lower().endswith('.csv') else f"{ruta}.csv"
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                #Usa la primera fila para definir los encabezados del CSV
                writer = csv.DictWriter(f, fieldnames=datos[0].keys())
                writer.writeheader()
                writer.writerows(datos)
        else:
            raise ValueError(f"Formato no soportado: {formato}")
        print(f"Archivo {file_path} guardado exitosamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")