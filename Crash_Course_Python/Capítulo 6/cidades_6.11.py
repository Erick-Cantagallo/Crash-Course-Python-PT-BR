# 6.11 Cidades: 
# Crie um dicionário chamado "cities". 
# Utilize o nome de três cidades como chaves de seu dicionário. 
# Crie um dicionário de informações sobre cada cidade e inclua o país em que a cidade está, 
# sua população aproximada e um fato sobre essa cidade. 
# O nome das chaves para o dicionário de cada cidade devem ser alguma coisa como 
# "country", "population" e "fact". 
# Exiba o nome de cada cidade e todas as informações que você armazenou a respeito.


cities = {
    'são paulo' : {
        'country' : 'brasil',
        'population' : '22.990.000 milhões',
        'fact' : 'A maior cidade do Brasil e da América do Sul.',
        },
    'tokyo' : {
        'country' : 'japão',
        'population' : '37.036.200 milhões',
        'fact' : 'A maior área metropolitana do mundo.',
        },
    'paris' : {
        'country' : 'frança',
        'population' : '2.113.705 milhões',
        'fact' : 'Conhecida como a "Cidade da Luz".',
        },
        }

for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact']
    print(f"\nCidade: {city.title()}")
    print(f"País: {country}")
    print(f"População: {population}")
    print(f"Fato: {fact}")
    