from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        list_repeat_companies = []
        companies = []
        companies_count = []
        complet_report = SimpleReport.generate(list)
        complet_report += "\nProdutos estocados por empresa:\n"

        for company in list:
            list_repeat_companies.append(company["nome_da_empresa"])
            if company["nome_da_empresa"] not in companies:
                companies.append(company["nome_da_empresa"])

        for company in companies:
            count = list_repeat_companies.count(company)
            companies_count.append(count)

        for index in range(len(companies)):
            complet_report += (
                f"- {companies[index]}: {companies_count[index]}\n"
            )

        return complet_report
