from generar.logica import crear_base_matriz, insertar_palabra, completar_con_aleatorios
from generar.visualizacion import imprimir_sopa

def menu_principal():
    #Gestiona el flujo de entrada, generación de la matriz y la opción de resolución para el usuario.
    palabras = []
    print("Bienvenido al Generador de Sopa de Letras del Dr. House")

    while len(palabras) < 15:
        entrada = input(f"Ingrese palabra {len(palabras)+1} (o 'FIN' para generar): ").strip()
        if entrada.upper() == 'FIN':
            break
        if len(entrada) > 15:
            print("Error: La palabra es muy larga.")
            continue
        if entrada:
            palabras.append(entrada)

    matriz = crear_base_matriz(15)
    indices_solucion = []
    
    for p in palabras:
        posiciones = insertar_palabra(matriz, p)
        if posiciones:
            indices_solucion.extend(posiciones)
    
    completar_con_aleatorios(matriz)

    imprimir_sopa(matriz)
    
    resolver = input("\n¿Desea ver la solución? (S/N): ")
    if resolver.upper() == 'S':
        imprimir_sopa(matriz, indices_solucion)

if __name__ == "__main__":
    menu_principal()