from inventory_report.importer.importer import Importer
from xmltodict import parse


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        file_type = path.split(".")[-1]
        if file_type != "xml":
            raise ValueError("Arquivo inválido")

        with open(path, 'r', encoding='utf-8') as file:
            xml_file = file.read()

            parsed_xml = parse(xml_file)

            xml_file_data = parsed_xml['dataset']['record']

        return xml_file_data
