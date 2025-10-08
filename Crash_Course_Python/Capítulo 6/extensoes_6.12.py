# 6.12 Extensões: 
# Agora que já estamos trabalhando com exemplos complexos o suficiente 
# para que sejam mais desenvolvidos de diferentes maneira, 
# use um dos programas de exemplo deste capítulo e o amplie, 
# adicionando chaves e valores novos, 
# alterando o contexto do programa ou melhorando a formatação da saída.


# Usando o programa favorite_languages.py como base, 
# adicione mais pessoas à pesquisa e mais linguagens favoritas.
# Em seguida, exiba os resultados ordenados por nome.

#Dicionário simples com pares chave-valor.
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    'alice' : 'java',
    'bob' : 'javascript',
    'carol' : 'go',
    'dave' : 'c++',
}

for name in sorted(favorite_languages.keys()):
    language = favorite_languages[name].title()
    print(f"A linguagem favorita do(a) {name.title()} é {language}.")
#----------------------------------------------------------------------------
# Um dicionário que contém listas como valores.
favorite_places = {
    'jen' : ['paris', 'londres', 'roma'],
    'sarah' : ['tóquio', 'seul'],
    'edward' : ['berlim', 'madrid', 'lisboa'],
    'phil' : ['nova york', 'los angeles'],
}

for name, places in favorite_places.items():
    print(f"\nOs lugares favoritos de {name.title()} são:")
    for place in places:
        print(f"- {place.title()}")