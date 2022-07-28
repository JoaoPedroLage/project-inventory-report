from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if (len(sys.argv) < 3):
        return sys.stderr.write("Verifique os argumentos\n")
    else:
        if sys.argv[1].endswith(".csv"):
            report = InventoryRefactor(CsvImporter)
        if sys.argv[1].endswith(".json"):
            report = InventoryRefactor(JsonImporter)
        if sys.argv[1].endswith(".xml"):
            report = InventoryRefactor(XmlImporter)

    return sys.stdout.write(report.import_data(sys.argv[1], sys.argv[2]))
