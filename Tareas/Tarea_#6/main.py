from generar.operaciones import generar_ejercicio
from generar.archivos import guardar_en_txt

def ejecutar_menu():
    print("--- Generador de Operaciones ---")
    
    cant_sumas = int(input("¿Cuántas sumas desea?: "))
    cant_restas = int(input("¿Cuántas restas desea?: "))
    cant_mult = int(input("¿Cuántas multiplicaciones desea?: "))
    cant_div = int(input("¿Cuántas divisiones desea?: "))

    practica = []
    respuestas = []
    config = {
        'suma': cant_sumas,
        'resta': cant_restas,
        'multiplicacion': cant_mult,
        'division': cant_div
    }

    for tipo, cantidad in config.items():
        for _ in range(cantidad):
            ej, res = generar_ejercicio(tipo)
            practica.append(ej)
            respuestas.append(res)

    guardar_en_txt("practica.txt", practica)
    guardar_en_txt("respuestas.txt", respuestas)
    
    print("\nLos archivos 'practica.txt' y 'respuestas.txt' fueron generados con éxito!")

if __name__ == "__main__":
    ejecutar_menu()