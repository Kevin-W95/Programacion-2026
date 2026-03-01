from generar.logica import crear_matriz, palabra, aleatorios
from generar.visualizacion import imprimir_sopa

def menu_principal():
    #El menú gestiona el flujo de entrada de datos.
    palabras = []
    print("--- Generador de Sopa de Letras - Dr. House ---")
    
    #Permitir al usuario ingresar palabras una por una
    while len(palabras) < 15:
        entrada = input(f"Ingrese palabra {len(palabras)+1} (o escriba 'SALIR' para terminar): ").strip()
        
        # Opción para finalizar el ingreso
        if entrada.upper() == 'SALIR':
            break
            
        if entrada:
            palabras.append(entrada)
        else: 
            print("Por favor, ingrese una palabra válida.")

    matriz = crear_matriz(15)
    indices_solucion = []
    
    for p in palabras:
        posiciones = palabra(matriz, p)
        if posiciones:
            indices_solucion.extend(posiciones)
    
    aleatorios(matriz)

    #Mostrar sopa para que el usuario intente resolverla
    print("\n¡Aquí está tu sopa de letras! Intenta encontrar las palabras.")
    imprimir_sopa(matriz)
    
    #Opción para mostrar la solución resaltada
    input("\nPresiona ENTER cuando estés listo para ver la solución...")
    print("\nSopa Resuelta (Palabras en color): ")
    imprimir_sopa(matriz, indices_solucion)

menu_principal()