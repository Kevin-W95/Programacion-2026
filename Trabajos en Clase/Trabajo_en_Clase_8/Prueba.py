from FileConverter import FileConverter

converter = FileConverter()

try:
    datos_json = converter.convertFromJson("ejemplo.json")
    print("Contenido JSON:", datos_json)
except FileNotFoundError:
    print("Error: No se encontró el archivo JSON.")

try:
    datos_csv = converter.convertFromCSV("ejemplo.csv")
    print("Contenido CSV:", datos_csv)
except FileNotFoundError:
    print("Error: No se encontró el archivo CSV.")

otra_instancia = FileConverter()
print(f"¿Son la misma instancia?: {converter is otra_instancia}")