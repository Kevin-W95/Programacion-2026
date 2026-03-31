""" Para ejecutar el codigo, escribir esto en una terminal nueva:
cd "Trabajos en Clase/Trabajo_en_Clase_6"

Despues presionar "Enter" y escribir: py main.py 
Presionar "Enter" otra vez y asi empezara el codigo """

from modulos.figuras_comp import Cilindro, Cono, Cubo, Esfera, Paralelepipedo
from procesos.liskov import imprimir_volumen

def main():
    figuras_dict = {
        "1": Cubo(5),
        "2": Paralelepipedo(4, 6, 2),
        "3": Cilindro(3, 7),
        "4": Esfera(4),
        "5": Cono(3, 9)
    }

    while True:
        print("\n--- CALCULADORA DE VOLUMEN ---")
        print("1. Volumen del cubo")
        print("2. Volumen del paralelepipedo")
        print("3. Volumen del cilindro")
        print("4. Volumen de la esfera")
        print("5. Volumen del cono")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Saliendo del programa...")
            break
        
        if opcion in figuras_dict:
            # Se aplica Liskov pasándole la figura seleccionada
            imprimir_volumen(figuras_dict[opcion])
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()