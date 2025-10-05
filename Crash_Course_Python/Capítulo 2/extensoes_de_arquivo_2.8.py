# 2.8 Extensões de arquivo: 
# O Python tem um método "removesuffix()" que funciona exatamente como "removeprefix()". 
# Atribua o valor 'python_notes.txt' a uma variável chamada filenam.
# Depois, utilize o método "removesuffix()" para exibir o nome do arquivo sem a extensão do arquivo, 
# como alguns navegadores de arquivos fazem. 


filename = 'python_notes.txt'

print(filename) # Nome original do Arquivo.
print(filename.removesuffix('.txt')) # Aqui remove o sufixo '.txt' e printa novamente o arquivo.