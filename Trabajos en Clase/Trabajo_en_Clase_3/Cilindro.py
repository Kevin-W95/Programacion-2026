def form_cilinder(r, h):
    return 3.14 * r**2 * h

def execute():
    print("\n--- Cálculo de Volumen: Cilindro ---")
    try: 
        R = float(input("Introduzca el valor del radio: "))  
        H = float(input("Introduzca el valor de la altura: "))  

        if R == 0 or H == 0:
            print("Error, introduzca otro valor que no sea 0")
        else:
            result = form_cilinder(R, H)
            print(f"El volumen del cilindro es: {result}")
    except ValueError:
        print("Error: Por favor, introduzca solo números.")

