from inventory_report.inventory.product import Product


def test_relatorio_produto():
    # pass  # Seu teste deve ser escrito aqui
    id = 1
    nome_do_produto = "Test product name"
    nome_da_empresa = "Test company name"
    data_de_fabricacao = "00-00-0000"
    data_de_validade = "00-00-0000"
    numero_de_serie = "123456789"
    instrucoes_de_armazenamento = "No instructions"

    report = f"""O produto {nome_do_produto}
        fabricado em {data_de_fabricacao}
        por {nome_da_empresa} com validade
        até {data_de_validade}
        precisa ser armazenado {instrucoes_de_armazenamento}."""

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert report == product.repr()
