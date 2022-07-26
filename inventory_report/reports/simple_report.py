from datetime import datetime, date


def date_to_seconds(date):
    date_split = date.split("-")
    epoch_time = datetime(
        int(date_split[0]), int(date_split[1]), int(date_split[2])
        )
    date_seg = epoch_time.timestamp()
    return date_seg


class SimpleReport:
    @classmethod
    def generate(cls, list):
        date_fab_list = []
        date_exp_list = []
        companies_list = []
        companies_count_list = []

        for product in list:
            date_fab_list.append(date_to_seconds(
                product['data_de_fabricacao'])
                )
            date_exp_list.append(date_to_seconds(
                product['data_de_validade'])
            )
            companies_list.append(product['nome_da_empresa'])

        for company in companies_list:
            count = companies_list.count(company)
            companies_count_list.append(count)

        company_products_number = max(companies_count_list)
        company_products_index = (
            companies_count_list.index(company_products_number)
        )

        company = companies_list[company_products_index]
        older_fab = date.fromtimestamp(min(date_fab_list))
        near_exp = date.fromtimestamp(min(date_exp_list))

        return (
                f'Data de fabricação mais antiga: {older_fab}\n'
                f'Data de validade mais próxima: {near_exp}\n'
                f'Empresa com mais produtos: {company}'
            )
