# 8.9 Mensagens: 
# Crie uma lista com uma série de mensagens curtas de texto. 
# Passe a lista para uma função chamada "show_messages()", 
# que exiba cada mensagem de texto.


def show_messages(mensagens):
    for mensagem in mensagens:
        print(mensagem)
mensagens = ["Olá, mundo!", "Python é incrível.", "Funções são úteis."]
show_messages(mensagens)
