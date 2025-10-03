# 3.6 Mais convidados: Você acabou de encontrar uma mesa maior de jantar,
# agora há mais espaço disponível. Convide mais três pessoas para o jantar.
#    - Comece com o programa do Exercício 3.4 ou 3.5. No final do programa, adicione um "print()",
#      informando às pessoas que encontrou uma mesa maior.
#    - Use um "insert()" para adicionar um convidado novo ao início de sua lista.
#    - Use um "insert()" para adicionar um convidado novo no meio de sua lista.
#    - Use um "append()" para adicionar um convidado novo no final de sua lista.
#    - Exiba um conjunto novo de mensagens de convite, um para cada pessoa em sua lista.
    

convidados = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print("Encontrei uma mesa maior de jantar, agora há mais espaço disponível.")
convidados.insert(0, "Nikola Tesla")
convidados.insert(2, "Galileu Galilei")
convidados.append("Ada Lovelace")
print(f"Olá, {convidados[0]}. Gostaria de convidá-lo para um jantar em minha casa.")
print(f"Olá, {convidados[1]}. Gostaria de convidá-lo para um jantar em minha casa.")
print(f"Olá, {convidados[2]}. Gostaria de convidá-lo para um jantar em minha casa.")
print(f"Olá, {convidados[3]}. Gostaria de convidá-lo para um jantar em minha casa.")
print(f"Olá, {convidados[4]}. Gostaria de convidá-lo para um jantar em minha casa.")
print(f"Olá, {convidados[5]}. Gostaria de convidá-lo para um jantar em minha casa.")