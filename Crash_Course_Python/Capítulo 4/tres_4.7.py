# 4.7 Três: 
# Crie uma lista dos múltiplos de 3, de 3 a 30. 
# Use um loop "for" para exibir os números em sua lista.


multiplos_de_tres = list(range(3, 31))
for numero in multiplos_de_tres:
    if numero % 3 == 0: # "==" serve para comparar valores.
        print(numero)

# Usando comparador "if" para verificar se o "resto da divisão" pelo número "3" é igual a zero.
# Se for igual a zero, significa que o número é múltiplo de 3 e será exibido.