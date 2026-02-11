def form_cone(r, h):
    return 1/3 * 3.14 * r**2 * h

def execute():
    print("\n--- Cálculo de Volumen: Cono ---")
    try:
        R = float(input("Introduzca el valor del radio: "))  
        H = float(input("Introduzca el valor de la altura: "))  

        if R == 0 or H == 0:
            print("Error, introduzca otro valor que no sea 0")
        else:
            result = form_cone(R, H)
            print(f"El volumen del cono es: {result}")
    except ValueError:
        print("Error: Por favor, introduzca solo números.")
