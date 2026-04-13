import json
import csv

class FileConverter:
    _instance = None

    def __new__(cls):
        #Garantiza que solo exista una única instancia 
        if cls._instance is None:
            cls._instance = super(FileConverter, cls).__new__(cls)
        return cls._instance

    def convertFromJson(self, jsonFileStr):
        """Lee un archivo JSON y lo retorna como diccionario"""
        with open(jsonFileStr, 'r', encoding='utf-8') as file:
            return json.load(file)

    def convertFromCSV(self, csvFileStr):
        """Lee un archivo CSV y lo retorna como diccionario"""
        with open(csvFileStr, mode='r', encoding='utf-8') as file:
            #DictReader convierte cada fila en un diccionario [cite: 14]
            reader = csv.DictReader(file)
            return [row for row in reader]