# 3.5 Mudando a lista de convidados: Você acabou de ficar sabendo que um dos convidados não conseguirá ir ao jantar,
# assim precisa enviar um conjunto novo de convites. É necessário convidar outra pessoa.
#    - Comece com o programa do Exercício 3.4. No final do programa, adicione um "print()",
#      informando o nome do convidado que não irá ao jantar.
#    - Modifique sua lista substituindo o nome do convidado que não pode comparecer
#      pelo nome da pessoa que você está convidando.
#    - Exiba um segundo conjunto de mensagens de convite,
#      uma para cada pessoa que ainda não consta em sua lista.


convidados = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print(f'O(A) Convidado(a) {convidados[1]} não poderá comparecer ao jantar.')
convidados[1] = "Nikola Tesla"
print(f'Olá {convidados[0]}, gostaria de convidá-lo para um jantar em minha casa.')
print(f'Olá {convidados[1]}, gostaria de convidá-lo para um jantar em minha casa.')
print(f'Olá {convidados[2]}, gostaria de convidá-lo para um jantar em minha casa.')