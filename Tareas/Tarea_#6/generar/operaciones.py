import random

def generar_ejercicio(tipo):
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    
    if tipo == 'suma':
        return f"{a}+{b}=", f"{a}+{b}={a+b}"
    elif tipo == 'resta':
        return f"{a}-{b}=", f"{a}-{b}={a-b}"
    elif tipo == 'multiplicacion':
        return f"{a}*{b}=", f"{a}*{b}={a*b}"
    elif tipo == 'division':
        resultado = a / b
        return f"{a}/{b}=", f"{a}/{b}={round(resultado, 2)}"