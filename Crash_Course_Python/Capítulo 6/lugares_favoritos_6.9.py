# 6.9 Lugares favoritos: 
# Crie um dicionário chamado "favorite_places". 
# Pense em três nomes para usar como chave no dicionário 
# e armazene de um a três lugares favoritos para cada pessoa. 
# Agora, para que este exercício fique ainda mais interessante, 
# peça a alguns amigos que lhe digam alguns de seus lugares favoritos. 
# Percorra o dicionário com um loop e exiba o nome de cada pessoa e seus lugares favoritos.


favorite_places = {
    'erick' : ['Canada', 'Japão', 'Russia'],
    'ana' : ['Itália', 'Espanha'],
    'gabriel' : ['Alemanha', 'Inglaterra', 'França'],
    'joão' : ['Portugal'],
    'felipe' : ['Egito', 'Filipinas', 'Indonésia'],
}
for nome, lugares in favorite_places.items():
    print(f"\nO(s) lugar(es) favorito(s) de {nome.title()} é(são):")
    for lugar in lugares:
        print(f"- {lugar}")
