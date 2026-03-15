from logica.system import (
    registrar_empleado, registrar_animal, 
    lista_empleados, lista_animales, listar_todo
)

def menu_animales():
    print("\n--- Agregar Animal ---")
    print("1. Reptil (Serpiente)\n2. Mamífero (León)\n3. Ave (Loro)\n4. Pez (Tiburón)\n5. Anfibio (Rana)") 
    tipo = input("Seleccione categoría: ")
    nom = input("Nombre del animal: ")
    ed = int(input("Edad: "))
    registrar_animal(tipo, nom, ed)

def main():
    while True:
        print("\n--- ADMINISTRACIÓN DEL ZOOLÓGICO ---")
        print("1. Agregar Empleado\n2. Listar Empleados") 
        print("3. Agregar Transporte\n4. Listar Transportes") 
        print("5. Agregar Animal\n6. Listar Animales")
        print("7. Salir")
        
        op = input("Seleccione una opción: ")
        
        if op == "1":
            pass 
        elif op == "2":
            listar_todo(lista_empleados)
        elif op == "5":
            menu_animales() 
        elif op == "6":
            listar_todo(lista_animales)
        elif op == "7":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main() 