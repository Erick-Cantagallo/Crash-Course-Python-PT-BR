# 8.12 Sanduíches: 
# Crie uma função que aceite uma lista de itens que uma pessoa quer em um sanduíche. 
# A função deve ter um parâmetro que colete todos os itens sendo solicitado. 
# Chame a função três vezes, com um número diferente de argumentos a cada vez.


def fazer_sanduiche(*itens): # O asterisco (*) na frente do parâmetro 'itens' informa 
                             # ao Python para coletar todos os argumentos posicionais 
                             # que vierem após os parâmetros formais em uma tupla chamada itens. 
                             # Isso permite que a função aceite qualquer número de argumentos.

    print("\nVocê pediu um sanduíche com os seguintes itens:")
    for item in itens:
        print(f"- {item}")
fazer_sanduiche('presunto', 'queijo', 'alface')
fazer_sanduiche('frango grelhado', 'tomate', 'maionese', 'picles')
fazer_sanduiche('atum', 'cebola', 'mostarda', 'alface', 'pimentão')
