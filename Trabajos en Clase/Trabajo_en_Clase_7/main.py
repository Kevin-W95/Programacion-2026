import os
import sys
from procesos import leer_csv, leer_json, calcular_promedios

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def menu():
    print("--- BIENVENIDO AL SISTEMA DE LEAD UNIVERSITY ---")
    print("1. Leer archivo CSV")
    print("2. Leer archivo JSON")
    
    opcion = input("Seleccione una opción (1 o 2): ")

    ruta_csv = os.path.join(BASE_DIR, "data", "personas.csv")
    ruta_json = os.path.join(BASE_DIR, "data", "personas.json")

    try:
        if opcion == "1":
            print(f"Abriendo: {ruta_csv}")
            datos = leer_csv(ruta_csv)
            resultados = calcular_promedios(datos)
            
        elif opcion == "2":
            print(f"Abriendo: {ruta_json}")
            datos = leer_json(ruta_json)
            resultados = calcular_promedios(datos)
            
        else:
            print("Opción no válida.")
            return

        if resultados:
            p_edad, p_salario, p_peso = resultados
            print("\n---RESULTADOS FINALES---")
            print(f"Promedio de Edad:    {p_edad:.2f} años")
            print(f"Promedio de Salario: {p_salario:.2f}")
            print(f"Promedio de Peso:    {p_peso:.2f} kg")
        
    except FileNotFoundError:
        print(f"\nERROR: No se encontró el archivo.")
        print(f"Asegúrate de que el archivo esté dentro de: {os.path.join(BASE_DIR, 'data')}")

if __name__ == "__main__":
    menu()