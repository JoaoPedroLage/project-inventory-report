from inventory_report.importer.importer import Importer
from json import load


class JsonImporter (Importer):
    @staticmethod
    def import_data(path):
        if path.split(".")[-1] != "json":
            raise ValueError("Arquivo inválido")

        with open(path, 'r', encoding='utf-8') as file:
            json_file_data = load(file)

        return json_file_data
