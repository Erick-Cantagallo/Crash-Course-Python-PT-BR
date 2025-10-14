# 8.5 Cidades: 
# Escreva uma função chamada "describe_city()" que aceite o nome de uma cidade e de seu país. 
# A função deve exibir uma simples frase, como "Reykjavik fica na Islândia". 
# Forneça ao parâmetro do país um valor default. 
# Chame sua função para três cidades diferentes e, 
# pelo menos, para uma que não esteja no país default.


def describe_city(city, country="Brasil"):
    """Exibe uma frase sobre a cidade e o país."""
    print(f"{city} fica no(a) {country}.")
describe_city("São Paulo")
describe_city("Londres", "Reino Unido")
describe_city("Paris", "França")
describe_city("Rio de Janeiro")
describe_city("Belo Horizonte")
describe_city("Salvador")
describe_city("Tóquio", "Japão")
