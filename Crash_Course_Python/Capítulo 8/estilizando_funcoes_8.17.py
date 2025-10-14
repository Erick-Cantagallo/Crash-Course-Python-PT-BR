# 8.17 Estilizando funções: 
# Escolha os três programas que você escreveu para este capítulo 
# e garanta que sigam as diretrizes de estilo descritas nesta seção.

# Exemplo de função estilizada 8.14

# Duas linhas vazias antes da definição da primeira função (se houver código acima)


def make_car(fabricante, modelo, **informacoes_adicionais):
    """
    Cria um dicionário contendo informações sobre um carro.                 #docstring
    Obriga o fabricante e o modelo, e aceita argumentos nomeados adicionais.
    """
    carro = {
        'fabricante': fabricante,
        'modelo': modelo
    }
    
    for chave, valor in informacoes_adicionais.items():
        carro[chave] = valor
    return carro


# Duas linhas vazias após o fim da função, antes da lógica principal


meu_carro = make_car('subaru', 'outback', cor='azul', pacote_reboque=True)
print(meu_carro)


# Se houver outra função, ela viria aqui, separada por duas linhas vazias.