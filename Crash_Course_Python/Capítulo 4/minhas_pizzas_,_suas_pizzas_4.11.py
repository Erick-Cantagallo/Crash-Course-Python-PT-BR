# 4.11 Minhas pizzas, suas pizzas: 
# Comece com o programa do Exercício 4.1. 
# Faça uma cópia da lista de pizzas e a nomeie como "friend_pizzas". 
# Em seguida, siga as etapas:
#    - Adicione uma pizza nova à lista original.
#    - Adicione uma pizza diferente à lista "friend_pizzas".
#    - Prove que tem duas listas separadas. 
#      Exiba a mensagem: 
#      "Minhas pizzas favoritas são:". 
#      Em seguida, use um loop "for" para exibir a primeira lista. 
#      Exiba a mensagem: 
#      "Minhas pizzas favoritas são:". 
#      E, em seguida, use um loop "for" para exibir a segunda lista. 
#      Garanta que cada pizza nova seja armazenada na lista adequada.


minhas_pizzas = ['mussarela', 'calabresa', 'portuguesa']
friend_pizzas = minhas_pizzas[:]  # Faz uma cópia da lista

#------------------------------------------------------------
minhas_pizzas.append('frango com catupiry')
friend_pizzas.append('pepperoni')
#------------------------------------------------------------
print('\nMinhas pizzas:')
print(minhas_pizzas)
print('\nPizzas do meu amigo:')
print(friend_pizzas)
#------------------------------------------------------------
print('\n')
print("Minhas pizzas favoritas são:")
for pizza in minhas_pizzas:
    print(f"- {pizza}")
print("\nAs pizzas favoritas do meu amigo são:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
#------------------------------------------------------------