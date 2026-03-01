from entidades.personas import Persona
from entidades.mascotas import Mascota
from entidades.vehiculo import Vehiculo

def ejecutar_simulacion():
    mi_auto = Vehiculo("Tesla", "2023")

    mi_perro = Mascota("Firulais", "Perro", 5)

    sujeto = Persona("Juan Perez", 30, "ACC-9988", mi_auto)

    print("--- PRUEBAS DE MÉTODOS ESPECIALES ---")

    print(sujeto)
    print(mi_perro)
    print(mi_auto)

    print(f"\nLongitud (Edad) de la persona: {len(sujeto)}")
    print(f"Longitud del nombre de la mascota: {len(mi_perro)}")

    print(f"\nAccediendo a atributo privado vía Getter: {mi_perro.nombre}")
    mi_perro.nombre = "Rex"
    print(f"Nombre de mascota modificado con Setter: {mi_perro.nombre}")

    if sujeto.vehiculo_asignado:
        print(f"\n{sujeto.nombre} está conduciendo un {sujeto.vehiculo_asignado.marca}")

if __name__ == "__main__":
    ejecutar_simulacion()