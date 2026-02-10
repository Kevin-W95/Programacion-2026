ingresar = input("Ingrese una palabro u oración de su preferencia: ").lower()

signs = ".,:;?!¿='"
for sign in signs:
    ingresar = ingresar.replace(sign, "")

word = ingresar.split()

stop = ["el", "la", "de", "y", "a", "un", "una"]
filter = []
for p in word:
    if p not in stop:
        filter.append(p)

frequent = {}
for p in filter:
    if p in frequent:
        frequent[p] += 1
    else:
        frequent[p] = 1

total = len(filter)
unique = len(frequent)

top = sorted(frequent.items(), key=lambda x: x[1], reverse=True)[:5]

print(f"\nCantidad total de palabras: {total}")
print(f"Cantidad de palabras únicas: {unique}")
print("Las 5 palabras más repetidas son: ")
for word, cuenta in top: 
    print(f"- {word}: {cuenta}")

