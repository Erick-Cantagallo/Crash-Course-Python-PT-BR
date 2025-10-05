# 4.6 Números ímpares: 
# Use o terceiro argumento da função "range()" 
# para criar uma lista com números ímpares de 1 a 20. 
# Use o loop "for" para exibir cada número.


for numero_impar in range(1, 21, 2):
    print(numero_impar)

# A chave para isso funcionar é que ele começa em "1" e pula de "2" em "2", caso começasse em "0",
# ele exibiria apenas números pares. Não possuí uma comparação direta para ver se é par ou ímpar,
# logo, se mudar o valor para "0", ele exibirá apenas números pares.