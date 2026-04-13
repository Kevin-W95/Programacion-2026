import json
import csv
import os

class FileConverter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileConverter, cls).__new__(cls)
            cls._instance.base_dir = os.path.dirname(os.path.abspath(__file__))
        return cls._instance

    def convertFromJson(self, jsonFileStr):
        ruta_completa = os.path.join(self.base_dir, jsonFileStr)
        
        with open(ruta_completa, 'r', encoding='utf-8') as file:
            return json.load(file)

    def convertFromCSV(self, csvFileStr):
        ruta_completa = os.path.join(self.base_dir, csvFileStr)
        
        with open(ruta_completa, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]