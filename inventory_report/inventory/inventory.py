from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        file_type = path.split(".")[-1]

        importer_method_type = {
            "csv": CsvImporter.import_data,
            "json": JsonImporter.import_data,
            "xml": XmlImporter.import_data,
        }

        options = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        data = importer_method_type[file_type](path)

        return options[type](data)
