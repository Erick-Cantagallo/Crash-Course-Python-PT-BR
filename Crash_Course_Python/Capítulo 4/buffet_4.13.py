# 4.13 Buffet: 
# Um restaurante com serviço de buffet oferece somente cinco refeições básicas. 
# Pense em cinco refeições simples e armazene-as em uma tupla.
#    - Use um loop "for" para exibir cada refeição que o restaurante oferece.
#    - Tente modififcar um dos elementos e ferifique se o Python rejeita a mudança.
#    - O restaurante muda seu cardápio, substituindo dois dos elementos por refeições diferentes. 
#      Adicione uma linha que reescreva a tupla e, depois, 
#      use um loop "for" para exibir cada um dos elementos no menu reformulado.


buffet = ("Lasanha", "Strogonoff", "Feijoada", "Churrasco", "Moqueca")
for comida in buffet:
    print(comida)
# buffet[0] = "Pizza" # Descomente esta linha para ver o erro 
# "TypeError: 'tuple' object does not support item assignment"
buffet = ("Pizza", "Strogonoff", "Feijoada", "Sushi", "Moqueca")
for comida in buffet:
    print(comida)