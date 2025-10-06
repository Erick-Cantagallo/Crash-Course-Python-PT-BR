# 5.9 Sem usuários: 
# Adicione um teste "if" a "hello_admin.py" a fim de garantir que a lista de usuários não esteja vazia.
#    - Se a lista estiver vazia, 
#      exiba a mensagem: "É necessário encontrar alguns usuários!"
#    - Remova todos os nomes de usuários de sua lista e verifique se a mensagem correta foi exibida.


users = []
# users = ['admin', 'erick', 'julia', 'ana', 'carol']
if users:
    for user in users:
        if user == 'admin':
            print("Olá administrador, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {user}, obrigado por fazer login novamente.")
else:
    print("É necessário encontrar alguns usuários!")