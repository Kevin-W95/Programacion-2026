def form_para(l, b, h):
    return l * b * h

def execute():
    print("\n--- Cálculo de Volumen: Paralelepipedo ---")
    try: 
        L = float(input("Introduzca el valor del lado: "))  
        B = float(input("Introduzca el valor de la base: "))  
        H = float(input("Introduzca el valor de la altura: "))  

        if L == 0 or B == 0 or H == 0:
            print("Error, introduzca otro valor que no sea 0")
        else: 
            result = form_para(L, B, H)
            print(f"El volumen del paralelepipedo es: {result}")
    except ValueError:
        print("Error: Por favor, introduzca solo números.")