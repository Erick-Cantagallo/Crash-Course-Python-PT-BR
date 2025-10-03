# 3.7 Reduzindo a lista de convidados: Você acabou de descobrir que sua mesa nova de jantar
# não chegará a tempo e agora tem espaço somente para dois convidados.
#    - Comece com o programa do Exercício 3.6. Adicione uma linha nova que exiba uma mensagem
#      que você pode convidar apenas duas pessoas para o jantar.
#    - Use o "pop()" para remover convidados de sua lista, um de cada vez, 
#      até que restem somente dois nomes nela. Sempre que remover um nome de sua lista,
#      exiba uma mensagem para essa pessoa informando que lamenta por não poder convidá-la para o jantar.
#    - Exiba uma mensagem para cada uma das duas pessoas que ainda estão na sua lista,
#      informando que ainda estão convidadas.
#    - Use o "del" para remover os dois últimos nomes de sua lista,
#      para que ela fique vazia. Exiba sua lista para ter certeza de que você realmente
#      tem uma lista vazia no final do seu programa. 


convidados = ['Nikola Tesla', 'Albert Einstein', 'Galileu Galilei', 'Marie Curie', 'Isaac Newton', 'Ada Lovelace']
print("Pessoal, infelizmente minha mesa nova de jantar não chegará a tempo e agora só posso convidar duas pessoas para o jantar.")
convidado_removido = convidados.pop()
print(f"Desculpe, {convidado_removido}, mas não posso convidá-lo(a) para o jantar.")
convidado_removido = convidados.pop()
print(f"Desculpe, {convidado_removido}, mas não posso convidá-lo(a) para o jantar.")
convidado_removido = convidados.pop()
print(f"Desculpe, {convidado_removido}, mas não posso convidá-lo(a) para o jantar.")
convidado_removido = convidados.pop()
print(f"Desculpe, {convidado_removido}, mas não posso convidá-lo(a) para o jantar.")
print(f"{convidados[0]}, você ainda está convidado(a) para o jantar.")
print(f"{convidados[1]}, você ainda está convidado(a) para o jantar.")
del convidados[1]
del convidados[0]
print(convidados)