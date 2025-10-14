# 8.7 Álbum: 
# Escreva uma função chamada "make_album()" que crie um dicionário 
# representando um álbum de música. 
# A função deve ter o nome de um artista e o título de álbum, 
# e deve retornar um dicionário com essas duas informações. 
# Utilize a função para cirar três dicionários representando álbuns distintos. 
# Exiba cada valor de retorno para mostrar que os dicionários 
# estão armazenando adequadamente as informações do álbum.
#
# Use "None" para adicionar um parâmetro
# opicional ao "make_album()" que possibilite armazenar 
# o número de músicas em um álbum. 
# Se a linha chamadora incluir um valor para o número de músicas, 
# adicione esse valor ao dicionário do álbum. 
# Crie, pelo menos, uma nova chamada de função que inclua o número de músicas em um álbum.


def make_album(nome_artista, titulo_album, numero_musicas=None):
    album = {
        'nome_artista': nome_artista,
        'titulo_album': titulo_album
    }
    if numero_musicas is not None:
        album['numero_musicas'] = numero_musicas
    return album
# Criando três dicionários representando álbuns distintos
album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon', 10)
album3 = make_album('Led Zeppelin', 'Led Zeppelin IV', 8)

# Exibindo os valores retornados
print(album1)
print(album2)
print(album3)

