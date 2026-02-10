#Primera parte 
def palindromos(text):
    clean = ""

    for character in text:
        if character.isalnum():
            clean += character.lower()

    reverse = clean[::-1]

    if clean == reverse:
        return True
    else:
        return False
    
print("Verificación de Palíndromos")
print("------------------------------------")
enter = input("Ingrese una palabra u oración: ")

if palindromos(enter):
    print(f"'{enter}' --> Es un palíndromo")
else:
    print(f"'{enter}' --> No es palíndromo")

print("")
print("-------------------------------- Separador --------------------------------------")
print("")

#Segunda parte

print("Hola! Bienvenido al contador de los números de la secuencia de Fibonacci.")

def fibonacci():
    enter = input("¿Cúantos números desea ver de la secuencia de Fibonacci? ")
    n = int(enter)

    if n <= 0:
        print("Error. Favor ingresar números superiores a 0")
    else: 
        a = 0
        b = 1

        result = []
    
    for i in range(n):
        result.append(str(a))
        next = a + b

        a = b
        b = next

    print("Aqui estan los números:", " ".join(result))

fibonacci()