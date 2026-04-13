from FileConverter import FileConverter 

converter = FileConverter()

#Método para JSON
try:
    datos_json = converter.convertFromJson("Trabajos en Clase/Trabajo_en_Clase_8/ejemplo.json")
    print("Contenido JSON:", datos_json)
except FileNotFoundError:
    print("Error: El archivo JSON no fue encontrado.")

#Método para CSV
try:
    datos_csv = converter.convertFromCSV("Trabajos en Clase/Trabajo_en_Clase_8/ejemplo.csv")
    print("Contenido CSV:", datos_csv)
except FileNotFoundError:
    print("Error: El archivo CSV no fue encontrado.")

#Verificación del Patrón Singleton
otra_instancia = FileConverter()
print(f"¿Son la misma instancia?: {converter is otra_instancia}")