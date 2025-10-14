# 8.8 Álbuns de usuários:
# Comece com seu programa do Exercício 8.7. 
# Escreva um loop "while" que possibilite aos usuários 
# inserir o artista e o título de um álbum. 
# Após receber essas informações, chame "make_album()" 
# com a entreda do usuário e exiba o dicionário criado. 
# Não se esqueça de incluir um valor de saída no "loop while"


def make_album(artista, titulo, n_músicas=None):
    album = {'artista': artista, 'título': titulo}
    if n_músicas:
        album['n_músicas'] = n_músicas
    return album
while True:
    print("\nPor favor, insira o nome do artista e do álbum:")
    print("(Digite 'sair' a qualquer momento para encerrar o programa)")
    
    artista = input("Artista: ")
    if artista.lower() == 'sair':
        break
    
    titulo = input("Título do álbum: ")
    if titulo.lower() == 'sair':
        break
    
    album = make_album(artista, titulo)
    print(f"\nDicionário do álbum criado: {album}")
