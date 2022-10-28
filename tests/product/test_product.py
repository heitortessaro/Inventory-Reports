from inventory_report.inventory.product import Product


def test_cria_produto():
    # pass  # Seu teste deve ser escrito aqui
    id = 1
    nome_do_produto = "Test product name"
    nome_da_empresa = "Test company name"
    data_de_fabricacao = "00-00-0000"
    data_de_validade = "00-00-0000"
    numero_de_serie = "123456789"
    instrucoes_de_armazenamento = "No instructions"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert id == product.id
    assert nome_do_produto == product.nome_do_produto
    assert nome_da_empresa == product.nome_da_empresa
    assert data_de_fabricacao == product.data_de_fabricacao
    assert data_de_validade == product.data_de_validade
    assert numero_de_serie == product.numero_de_serie
    assert instrucoes_de_armazenamento == product.instrucoes_de_armazenamento
