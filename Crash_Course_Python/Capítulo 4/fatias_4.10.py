# 4.10 Fatias: 
# Use um dos programas que você escreveu neste capítulo, 
# adicione diversas linhas ao final do programa para executarem o seguinte:
#    - Exiba a mensagem: "Os três primeiros elementos da lista são:". 
#      Em seguida use uma fatia para exibir os três primeiros elementos da lista desse programa.
#    - Exiba a mensagem: "Os três elementos que ficam no meio da lista são:". 
#      Depois, use uma fatia para exibir os três elementos do meio da lista.
#    - Exiba a mensagem: "Os três últimos elementos da lista são:". 
#      Em seguida, utilize uma fatia para exibir os três últimos elementos da lista.


numeros = list(range(1, 21))
#-------------------------------------------------------------------
print("Os três primeiros elementos da lista são:")
print(numeros[:3])
#-------------------------------------------------------------------

print("Os três elementos que ficam no meio da lista são:")
meio = len(numeros) // 2
print(numeros[meio-1:meio+2])

# Explicação da lógica para solucionar o "problema do meio":

# Para uma lista com um número par de elementos (como 20), 
# onde o "meio" não é um único número, 
# a sua lógica captura os três números centrais (9, 10, 11) de forma robusta.

# len(numeros) é 20.

# meio = 20 // 2 é 10. (Este é o índice do 11º elemento, que é o número 11).

# O fatiamento numeros[10-1 : 10+2] se torna numeros[9:12].

# O índice 9 contém o número 10.

# O índice 10 contém o número 11.

# O índice 11 contém o número 12.

# A fatia resultante é [10, 11, 12], que são os três números centrais.

#-------------------------------------------------------------------
print("Os três últimos elementos da lista são:")
print(numeros[-3:])
#-------------------------------------------------------------------