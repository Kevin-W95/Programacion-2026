import Encriptación, Desencriptación

def execute():
    print("\n--- MODULO CÉSAR ---")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")

    selec = input("Seleccione su acción: ")

    if selec in ["1", "2"]:
        msg = input("Ingrese el texto: ")
        try:
            slide = int(input("Ingrese el factor de desplazamiento (N): "))
            if selec == "1":
                print(f"Frase encriptada: {Encriptación.cesar_encryp(msg, slide)}")
            else: 
                print(f"Frase desencriptada: {Desencriptación.cesar_decrypt(msg, slide)}")
        except ValueError:
            print("Error: Introducir números enteros para realizar el desplazamiento.")
    else: 
        print("Opción Inválida.")
