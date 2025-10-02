# 2.7 Removendo nomes: Use uma variável para representar o nome de uma pessoa e inclua alguns caracteres de espaço em branco no início e no final do nome. 
# Lembre-se de usar cada combinação de caracteres, "/t" e "/n", pelomenos uma vez. Exiba o nome uma vez para que o espaço em branco ao redor do nome seja mostrado.
# Em seguida, printe o nome usando cada uma das três funções de remoção, "lstrip()", "rstrip()" e "strip()".

""""
\t → significa tabulação horizontal (tipo quando você aperta a tecla TAB no teclado).
\n → significa quebra de linha (line break). Ou seja, o texto vai terminar e pular pra linha de baixo.
"""
"""
O propósito é justamente você ver como o Python trata esses espaços e quebras quando usa:
Ou seja, o \t e o \n são exemplos de "whitespace characters" (caracteres de espaço em branco invisíveis). 
Eles existem, ocupam espaço, mas não aparecem como letras.
"""

nome = "\t   Caio Júlio César.   \n"

print("Nome original:")
print(nome)  # aqui você já vai ver o tab no começo e a quebra de linha no fim

print("Com lstrip():")
print(nome.lstrip())

print("Com rstrip():")
print(nome.rstrip())

print("Com strip():")
print(nome.strip())

