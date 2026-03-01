def imprimir_sopa(matriz, resaltados=None):
    #Imprime la sopa de letras en consola.
    #Si se pasa una lista de "resaltados", imprime esas letras en color azul.

    #Coloración
    COLOR_AZUL = '\033[94m'
    RESET = '\033[0m'
    
    print("\n--- SOPA DE LETRAS ---")
    for f in range(len(matriz)):
        linea = ""
        for c in range(len(matriz[f])):
            if resaltados and (f, c) in resaltados:
                linea += f"{COLOR_AZUL}{matriz[f][c]}{RESET} "
            else:
                linea += f"{matriz[f][c]} "
        print(linea)