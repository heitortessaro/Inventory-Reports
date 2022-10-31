from inventory_report.reports.simple_report import SimpleReport
from collections import Counter

# Used materials:
# - https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
# - https://realpython.com/python-counter/


class CompleteReport(SimpleReport):
    @classmethod
    def companies_and_product_quantities(cls, product_list):
        companies = [product["nome_da_empresa"] for product in product_list]
        companies_and_product_quantities = dict(Counter(companies))
        return companies_and_product_quantities

    @classmethod
    def generate(cls, product_list):
        most_frequent_company = CompleteReport.most_frequent_company(
            product_list
        )
        oldest_product = CompleteReport.oldest_product(product_list)
        closest_to_expiration = CompleteReport.closest_to_expiration(
            product_list
        )
        companies_and_product_quantities = (
            CompleteReport.companies_and_product_quantities(product_list)
        )
        output_list = ""
        for key, value in companies_and_product_quantities.items():
            output_list += f"- {key}: {value}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_to_expiration}\n"
            f"Empresa com mais produtos: {most_frequent_company}\n"
            f"Produtos estocados por empresa:\n"
            f"{output_list}"
        )
