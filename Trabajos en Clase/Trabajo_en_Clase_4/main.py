from entidades.personas import Persona
from entidades.mascotas import Mascota
from entidades.vehiculo import Vehiculo

def mostrar_menu():
    print("\n--- MUNDO VIRTUAL SIMS ---")
    print("1. Crear persona")
    print("2. Crear mascota")
    print("3. Crear vehículo")
    print("4. Imprimir personas")
    print("5. Imprimir mascotas")
    print("6. Imprimir vehículos")
    print("7. Imprimir todas las entidades")
    print("8. Salir")
    return input("Seleccione una opción: ")

def main():
    # Listas para almacenar los datos
    personas = []
    mascotas = []
    vehiculos = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            profesion = input("Profesión: ")
            personas.append(Persona(nombre, edad, profesion))
            print("Persona creada con éxito.")

        elif opcion == "2":
            nombre = input("Nombre de la mascota: ")
            especie = input("Especie (Perro, Gato, etc.): ")
            edad = input("Edad: ")
            mascotas.append(Mascota(nombre, especie, edad))
            print("Mascota registrada.")

        elif opcion == "3":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            vehiculos.append(Vehiculo(marca, modelo, color))
            print("Vehículo añadido.")

        elif opcion == "4":
            print("\n--- LISTA DE PERSONAS ---")
            for p in personas: print(p)

        elif opcion == "5":
            print("\n--- LISTA DE MASCOTAS ---")
            for m in mascotas: print(m)

        elif opcion == "6":
            print("\n--- LISTA DE VEHÍCULOS ---")
            for v in vehiculos: print(v)

        elif opcion == "7":
            print("\n--- TODAS LAS ENTIDADES ---")
            for e in personas + mascotas + vehiculos:
                print(e)

        elif opcion == "8":
            print("Saliendo del simulador... ¡Adiós!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()