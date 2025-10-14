def make_car(fabricante, modelo, **informacoes_adicionais):
    """Cria um dicionário representando um carro."""
    carro = {
        'fabricante': fabricante,
        'modelo': modelo
    }
    for chave, valor in informacoes_adicionais.items():
        carro[chave] = valor
    return carro