from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.split(".")[-1] != "csv":
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            data = csv.DictReader(file)

            return [row for row in data]
