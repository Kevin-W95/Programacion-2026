import random
import string

def crear_base_matriz(tamano=15):
    #Esta función crea una matriz cuadrada de n x n inicializada con espacios vacíos para ser llenada despues.
    return [[' ' for _ in range(tamano)] for _ in range(tamano)]

def insertar_palabra(matriz, palabra):
    tamano = len(matriz)
    palabra = palabra.upper()
    intentos = 0
    
    while intentos < 100:
        fila = random.randint(0, tamano - 1)
        col = random.randint(0, tamano - len(palabra))
        
        # Verificador
        if all(matriz[fila][col + i] == ' ' for i in range(len(palabra))):
            posiciones = []
            for i in range(len(palabra)):
                matriz[fila][col + i] = palabra[i]
                posiciones.append((fila, col + i))
            return posiciones
        intentos += 1
    return None

def completar_con_aleatorios(matriz):
    abc = string.ascii_uppercase
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if matriz[f][c] == ' ':
                matriz[f][c] = random.choice(abc)