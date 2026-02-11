def form_sphere(r):
    return 4/3 * 3.14 * r**3

def execute():
    print("\n--- Cálculo de Volumen: Esfera ---")
    try:
        R = float(input("Introduzca el valor del radio: "))  

        if R == 0:
            print("Error, introduzca otro valor que no sea 0")
        else: 
            result = form_sphere(R)
            print(f"El volumen de la esfera es: {result}")
    except ValueError:
        print("Error: Por favor, introduzca solo números.")