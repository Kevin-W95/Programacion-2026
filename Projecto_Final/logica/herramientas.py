import os

def validar_no_vacio(texto, nombre_campo):
    """Verifica que el usuario no deje campos obligatorios en blanco"""
    if not texto.strip():
        raise ValueError(f"Error: El campo '{nombre_campo}' no puede estar vacío.")
    return texto

def leer_numero_positivo(mensaje, es_entero=False):
    """
    Maneja excepciones para asegurar que el usuario ingrese números válidos y positivos
    """
    while True:
        try:
            valor = input(mensaje)
            numero = int(valor) if es_entero else float(valor)
            if numero < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def limpiar_pantalla():
    """Mantiene la consola limpia para una mejor experiencia de usuario."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_id_unico(id_nuevo, catalogo):
    """
    Recorre el catálogo para asegurar que el identificador no esté repetido
    """
    for juego in catalogo:
        if juego._id == id_nuevo:
            raise ValueError("Error: El Identificador ya existe en el catálogo.")
    return id_nuevo