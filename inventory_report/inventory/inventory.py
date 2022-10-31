import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_file(cls, path):
        partial_path = path[-5:]
        if ".csv" in partial_path:
            return Inventory.read_csv(path)

    @classmethod
    def read_csv(cls, path):
        with open(path, encoding="utf-8") as file:
            product_list = []
            for row in csv.DictReader(file, delimiter=",", quotechar='"'):
                product_list.append(row)
        return product_list

    @classmethod
    def import_data(cls, path, report_type):
        product_list = Inventory.import_file(path)
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        if report_type == "completo":
            return CompleteReport.generate(product_list)
