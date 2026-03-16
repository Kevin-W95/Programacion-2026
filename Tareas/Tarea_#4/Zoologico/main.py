from logica.system import (
    registrar_empleado, registrar_animal, registrar_transporte, listar_todo, lista_empleados, lista_animales, lista_transportes
)

def menu_empleados():
    print("\n--- Agregar Empleado ---")
    print("1. Administrador\n2. Guardian\n3. Conserje\n4. Veterinario")
    tipo = input("Seleccione tipo (1-4): ")
    nom = input("Nombre del empleado: ")
    ide = input("ID de empleado: ")
    registrar_empleado(tipo, nom, ide)
    print("Empleado registrado con éxito.")

def menu_animales():
    print("\n--- Agregar Animal ---")
    print("1. Reptil (Serpiente)\n2. Mamífero (León)\n3. Ave (Loro)\n4. Pez (Tiburón)\n5. Anfibio (Rana)") 
    tipo = input("Seleccione categoría: ")
    nom = input("Nombre del animal: ")
    ed = int(input("Edad: "))
    registrar_animal(tipo, nom, ed)

def menu_transportes():
    print("\n--- Agregar Transporte ---")
    print("1. Bicicleta\n2. Cuadraciclo\n3. Patineta")
    tipo = input("Seleccione tipo: ")
    cod = input("Código de identificación: ")
    registrar_transporte(tipo, cod)

def main():
    while True:
        print("\n--- ADMINISTRACIÓN DEL ZOOLÓGICO ---")
        print("1. Agregar Empleado\n2. Listar Empleados") 
        print("3. Agregar Transporte\n4. Listar Transportes") 
        print("5. Agregar Animal\n6. Listar Animales")
        print("7. Salir")
        
        op = input("Seleccione una opción: ")
        
        if op == "1":
            menu_empleados() 
        elif op == "2":
            listar_todo(lista_empleados)
        elif op == "3":
            menu_transportes()
        elif op == "4":
            listar_todo(lista_transportes)
        elif op == "5":
            menu_animales() 
        elif op == "6":
            listar_todo(lista_animales)
        elif op == "7":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main() 