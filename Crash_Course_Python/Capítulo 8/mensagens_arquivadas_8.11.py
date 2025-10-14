# 8.11 Mensagens arquivadas: 
# Comece sua tarefa a partir do Exercício 8.10. 
# Chame a função "send_messages()" com uma cópia da lista de mensagens. 
# Após chamar a função, exiba ambas as listas 
# para mostrar que a lista original reteve suas mensagens.


def show_messages(mensagens):
    for mensagem in mensagens:
        print(mensagem)

def send_messages(mensagens, sent_messages):
    while mensagens:
        mensagem_atual = mensagens.pop()
        print(mensagem_atual)
        sent_messages.append(mensagem_atual)
mensagens = ["Olá, mundo!", "Python é incrível.", "Funções são úteis."]
sent_messages = []
send_messages(mensagens[:], sent_messages)
print("\nMensagens originais:")
print(mensagens)
print("\nMensagens enviadas:")
print(sent_messages)
# Usando mensagens[:] para passar uma cópia da lista original
# para que a lista original retenha suas mensagens.
print("\nVerificando se a lista original manteve suas mensagens:")
show_messages(mensagens)
print("\nVerificando as mensagens enviadas:")
show_messages(sent_messages)