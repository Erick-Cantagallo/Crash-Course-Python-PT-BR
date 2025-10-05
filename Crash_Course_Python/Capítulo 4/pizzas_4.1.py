# 4.1 Pizzas: 
# Pense em, pelo menos, três tipos que você gosta. 
# Armazene esses nomes de pizza em uma lista e use um loop "for" para exibir o nome de cada uma.
#    - Modifique seu loop "for" a fim de que exiba uma frase usando o nome da pizza, 
#      em vez de exibir apenas o nome da pizza. Para cada pizza,
#      você deve gerar uma linha de saída com uma simples afirmação 
#      como: "Gosto de pizza de pepperoni".
#    - Adicione uma linha no final do seu programa,
#      fora do loop "for", que ressalte o quanto você gosta de pizza. 
#      A saída deve ter três ou mais linhas sobre os tipos de pizza que você gosta e,
#      em seguida, uma frase adicional, como "Eu amo pizza!".


pizzas = ['mussarela', 'calabresa', 'portuguesa']
for pizza in pizzas:
    print(pizza)
#--------------------------------------------
print('\n')
for pizza in pizzas:
    print(f'Gosto de pizza de {pizza}.')
print('Eu amo Pizza!')