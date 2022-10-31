import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path) as xml_file:
            return xmltodict.parse(xml_file.read())["dataset"]["record"]
