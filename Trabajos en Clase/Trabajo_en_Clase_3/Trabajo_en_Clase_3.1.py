import Cono, Esfera, Cubo, Cilindro, Paralelepipedo

def calc_vol():
    while True:
        print("--- MENÚ DE VOLÚMENES ---")
        print("1. Cubo\n2. Esfera\n3. Cono\n4. Cilindro\n5. Paralelepipedo\n6. Terminar")
        
        selec = input("Seleccione la operación (1-5): ")
        
        if selec == "1":
            Cubo.execute() 
        elif selec == "2": 
            Esfera.execute()
        elif selec == "3": 
            Cono.execute()
        elif selec == "4": 
            Cilindro.execute()
        elif selec == "5": 
            Paralelepipedo.execute()
        elif selec == "6":
            print("¡Gracias por elegirnos. Esperamos verte de nuevo!")
            break
        else: 
            print("Finalizando programa..")
            exit()

if __name__ == "__main__":
    calc_vol()
