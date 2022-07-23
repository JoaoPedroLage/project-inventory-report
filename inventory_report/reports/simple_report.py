from datetime import datetime


class SimpleReport:
    def generate(list):
        products_list = []

        for product in list:
            products_list.append(product['data_de_fabricacao'])
            