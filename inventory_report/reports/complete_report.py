from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        companies = []
        companies_list = []
        companies_count_list = []
        complet_report = SimpleReport.generate(lista)
        complet_report += "\nProdutos estocados por empresa:\n"

        for company in lista:
            companies_list.append(company['nome_da_empresa'])
            if company['nome_da_empresa'] not in companies:
                companies.append(company['nome_da_empresa'])

        for company in companies:
            count = companies_list.count(company)
            companies_count_list.append(count)

        companies_list = list(dict.fromkeys(companies_list))

        for index in range(len(companies)):
            complet_report += (
                f"- {companies[index]}: {companies_count_list[index]}\n"
            )

        return complet_report
