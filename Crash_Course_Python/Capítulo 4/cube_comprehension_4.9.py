# 4.9 Cube Comprehension: 
# Use uma list comprehension para gerar uma lista dos primeiros 10 cubos.


# Explicação rápida do que é uma list comprehension:
# Uma list comprehension é uma maneira concisa de criar listas em Python. 
# Ela permite que você crie uma nova lista aplicando uma expressão a cada item 
# de uma sequência ou iterável, tudo em uma única linha de código.
# A sintaxe básica de uma list comprehension é:
# nova_lista = [expressão for item in iterável if condição]
# Onde:
# - "expressão": é o valor que você deseja adicionar à nova lista.
# - "item": é a variável que representa cada elemento do iterável.
# - "iterável": é a sequência ou coleção de elementos que você está percorrendo (como uma lista, tupla, etc.).
# - "condição" (opcional): é uma expressão booleana que filtra os itens do iterável. 
#   Apenas os itens que satisfazem a condição serão incluídos na nova lista.

cubos = [x**3 for x in range(1, 11)]
print(cubos)