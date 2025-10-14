# 8.10 Enviando mensagens: 
# Comece com uma cópia de seu programa do Exercício 8.9. 
# Escreva uma função chamada "send_messages()" para exibir cada mensagem de texto 
# e passe cada mensagem para uma nova lista chamada "sent_messages" à medida que é exibida. 
# Após chamar a função, exiba ambas as listas para ter certeza 
# de que as mensagens foram corretamente transferidas.


def show_messages(mensagens):
    for mensagem in mensagens:
        print(mensagem)
def send_messages(mensagens, sent_messages):
    while mensagens:
        mensagem = mensagens.pop()
        print(mensagem)
        sent_messages.append(mensagem)
mensagens = ["Olá, mundo!", "Python é incrível.", "Funções são úteis."]
sent_messages = []
send_messages(mensagens[:], sent_messages)
print("\nMensagens:")
show_messages(mensagens)
print("\nMensagens enviadas:")
show_messages(sent_messages)
# Note que ao chamar a função send_messages,
# passamos uma cópia da lista mensagens usando mensagens[:]
# Isso é feito para preservar a lista original de mensagens,
# já que a função send_messages modifica a lista removendo os itens dela.
# Assim, após a chamada da função, a lista mensagens original permanece inalterada.
# Se você não se importar em perder a lista original de mensagens,
# você pode simplesmente passar mensagens sem os colchetes.
# Isso fará com que a lista mensagens seja esvaziada após a chamada da função.