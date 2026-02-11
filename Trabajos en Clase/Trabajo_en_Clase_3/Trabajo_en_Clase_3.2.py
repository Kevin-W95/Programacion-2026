import Encriptación, Desencriptación, Cesar

def menú():
    while True:
        print("\n================================")
        print("    SISTEMA DE ENCRIPTACIÓN")
        print("================================")
        print("1. Usar Cifrado César")
        print("2. Salir")

        selec = input("\nSeleccione una opción:")

        if selec == "1":
            Cesar.execute()
        elif selec == "2":
            print("Terminando programa..")
            break
        else: 
            print("Ingresar una opción válida")

if __name__ == "__main__":
    menú()