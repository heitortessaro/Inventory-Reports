from datetime import date

# from datetime import datetime
from collections import Counter

# Used materials:
# - https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
# - https://realpython.com/python-counter/


class SimpleReport:
    @classmethod
    def most_frequent(cls, List):
        occurence_count = Counter(List)
        # get de most common and return just the value
        return occurence_count.most_common()[0][0]

    @classmethod
    def most_frequent_company(cls, product_list):
        companies = [product["nome_da_empresa"] for product in product_list]
        return SimpleReport.most_frequent(companies)

    @classmethod
    def oldest_product(cls, product_list):
        fabrication_date = [
            date.fromisoformat(product["data_de_fabricacao"])
            for product in product_list
        ]
        return min(fabrication_date)

    # @classmethod
    # def oldest_product(cls, product_list):
    #     fabrication_date = [
    #         datetime.fromisoformat(product["data_de_fabricacao"]).date()
    #         for product in product_list
    #     ]
    #     return min(fabrication_date)

    @classmethod
    def closest_to_expiration(cls, product_list):
        expiration_date = [
            date.fromisoformat(product["data_de_validade"])
            for product in product_list
            if date.fromisoformat(product["data_de_validade"]) > date.today()
        ]
        return min(expiration_date)

    @classmethod
    def generate(cls, product_list):
        most_frequent_company = SimpleReport.most_frequent_company(
            product_list
        )
        oldest_product = SimpleReport.oldest_product(product_list)
        closest_to_expiration = SimpleReport.closest_to_expiration(
            product_list
        )

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_to_expiration}\n"
            f"Empresa com mais produtos: {most_frequent_company}"
        )
