def guardar_en_txt(nombre_archivo, lista_ejercicios):
    with open(nombre_archivo, "w") as f:
        for linea in lista_ejercicios:
            f.write(f"{linea}\n") 