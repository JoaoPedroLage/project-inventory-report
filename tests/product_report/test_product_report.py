from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "best product",
        "mindset company",
        "01/07/2022",
        "01/07/2023",
        "0123456789",
        "store in a cool place, away from the sun",
    )

    slice01 = f"O produto {product.nome_do_produto}"
    slice02 = f" fabricado em {product.data_de_fabricacao}"
    slice03 = f" por {product.nome_da_empresa} com validade"
    slice04 = f" até {product.data_de_validade}"
    slice05 = f" precisa ser armazenado {product.instrucoes_de_armazenamento}."

    string = slice01 + slice02 + slice03 + slice04 + slice05

    assert str(product) == string
