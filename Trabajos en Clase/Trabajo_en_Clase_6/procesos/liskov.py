def imprimir_volumen(figura):
    """
    Principio de Liskov: Esta función puede recibir cualquier objeto 
    hijo de Figura y funcionará correctamente sin conocer su tipo específico.
    """
    resultado = figura.volumen()
    print(f"\n>>> El volumen es: {resultado:.2f}")