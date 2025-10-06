# 5.8 Olá, admin: 
# Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome "admin". 
# Imagine que está escrevendo um código que exibirá uma mensagem de boas-vindas aos usuários, 
# após cada um deles logar em um site. 
# Percorra a lista com um loop e exiba uma mensagem de boas-vindas para cada usuário.
#    - Se o nome de usuário for "admin", exiba uma mensagem especial, 
#      tipo: "Olá administrador, gostaria de ver um relatório de status?"
#    - Caso contrário, exiba uma mensagem genérica, 
#      como: "Olá Jaden, obrigado por fazer login novamente."


usernames = ['admin', 'erick', 'maria', 'joao', 'ana']
for username in usernames:
    if username == 'admin':
        print("Olá administrador, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {username}, obrigado por fazer login novamente.")
