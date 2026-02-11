def form_cube(l, l2, l3):
    return l * l2 * l3

def execute():
    print("\n--- Cálculo de Volumen: Cubo ---")
    try: 
        L = float(input("Introduzca el valor del primer lado: "))
        L2 = float(input("Introduzca el valor del primer lado: "))
        L3 = float(input("Introduzca el valor del primer lado: "))

        if L == 0 or L2 == 0 or L3 == 0:
            print("Error: Introduzca otro valor que no sea 0")
        else: 
            result = form_cube(L, L2, L3)
            print(f"El volumen del cubo es: {result}")

    except ValueError:
        print("Error: Por favor, introduzca solo números.")

        