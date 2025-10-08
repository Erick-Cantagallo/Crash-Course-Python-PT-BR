# 6.3 Glossário: 
# Um dicionário Python pode ser usado para modelar um dicionário real. 
# Contudo, para evitar confusão, vamos chamá-lo de glossário.
#    - Pense em cinco palavras do mundo de programação que você aprendeu nos capítulos anteriores. 
#      Use essas palavras como chaves em seu glossário e armazene seus significados como valores.
#    - Exiba cada palavra e seu significado como uma saída elegantemente formatada. 
#      É possível até mesmo exibir a palavra seguida por dois-pontos 
#      e depois seu significado ou a palavra em uma linha e, em seguida, 
#      exibir seu significado indentado em uma segunda linha. 
#      Use o caractere quebra de linha "(\n)" para inserir uma linha em branco 
#      entre cada par palavra-significado em sua saída.


glossario = {
    'variável': 'Um nome que se refere a um valor armazenado na memória do computador.',
    'lista': 'Uma coleção ordenada e mutável de itens, que pode conter elementos de diferentes tipos.',
    'dicionário': 'Uma coleção não ordenada de pares chave-valor, onde cada chave é única.',
    'loop': 'Uma estrutura de controle que permite repetir um bloco de código várias vezes.',
    'função': 'Um bloco de código reutilizável que realiza uma tarefa específica e pode receber entradas e retornar saídas.'
}

print(f"Variável:\n\t{glossario['variável']}\n")
print(f"Lista:\n\t{glossario['lista']}\n")
print(f"Dicionário:\n\t{glossario['dicionário']}\n")
print(f"Loop:\n\t{glossario['loop']}\n")
print(f"Função:\n\t{glossario['função']}\n")
