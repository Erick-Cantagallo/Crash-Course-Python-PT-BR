# 6.8 Animais de Estimação: 
# Crie vários dicionários, 
# em que cada dicionário representa um animal de estimação diferente. 
# Em cada dicionário inclua o tipo  de animal e o nome do dono. 
# Armazene esses dicionários em uma lista chamada "pets". 
# Depois, percorra sua lista com um loop e, enquanto faz isso, 
# exiba tudo o que sabe sobre cada animal de estimação.


animal_1 = {
    'tipo' : 'cachorro',
    'nome' : 'toy',
    'dono' : 'erick',
}
animal_2 = {
    'tipo' : 'gato',
    'nome' : 'whisky',
    'dono' : 'jenifer',
}
animal_3 = {
    'tipo' : 'papagaio',
    'nome' : 'josé',
    'dono' : 'Ana',
}
pets = [animal_1, animal_2, animal_3]

for pet in pets:
    tipo = pet['tipo']
    nome = pet['nome']
    dono = pet['dono']
    print(f"\nTipo de animal: {tipo.title()}")
    print(f"Nome do animal: {nome.title()}")
    print(f"Dono do animal: {dono.title()}")
