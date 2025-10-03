# 3.11 Erro intencional: Se você ainda não recebeu um erro de índice em um dos seus programas, 
# tente gerar um. Mude um índice em um de seus programas para gerar um erro de índice. 
# Faça questão de corrigir o erro antes de fechar o programa.

lista = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
# Isso gerará um erro de índice.
print(lista[10]) # Depois de ver o erro, comente ou remova esta linha.
#-------------------------------------------------
# Corrigindo o erro
print(lista[2])  # Acessando um índice válido.
#-------------------------------------------------
# Saída do erro:
# Traceback (most recent call last):
#   File "erro_intencional_3.11.py", line 7, in <module>
#     print(lista[10])  # Isso gerará um erro de índice
# IndexError: list index out of range
#-------------------------------------------------
# Saída corrigida: 
# C++
