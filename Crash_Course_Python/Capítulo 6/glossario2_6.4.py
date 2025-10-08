# 6.4 Glossário 2: 
# Agora você sabe como percorrer um dicionário com um loop, 
# limpe o código do exercício 6.3 substituindo sua série de print() 
# por um loop que percorre as chaves e o valor do dicionário. 
# Quando tiver certeza de que seu loop funciona, 
# adicione mais cinco termos Python ao seu glossário. 
# Quando executar seu programa novamente, essas palavras 
# e dignificados novos devem ser incluídos automaticamente na saída.



glossario = {
    'variável': 'Um nome que se refere a um valor armazenado na memória do computador.',
    'lista': 'Uma coleção ordenada e mutável de itens, que pode conter elementos de diferentes tipos.',
    'dicionário': 'Uma coleção não ordenada de pares chave-valor, onde cada chave é única.',
    'loop': 'Uma estrutura de controle que permite repetir um bloco de código várias vezes.',
    'função': 'Um bloco de código reutilizável que realiza uma tarefa específica e pode receber entradas e retornar saídas.'
}

for palavra, significado in glossario.items():
    print(f"{palavra.title()}:\n\t{significado}\n")
print('\n')
glossario['tupla'] = 'Uma coleção ordenada e imutável de elementos.'
glossario['classe'] = 'Um modelo para criar objetos que encapsulam dados e comportamentos.'
glossario['método'] = 'Uma função associada a um objeto.'
glossario['condicional'] = 'Permite executar blocos de código dependendo de uma condição.'
glossario['importação'] = 'Traz módulos externos para o programa.'
print('-'*90)
print('\n\tAtualizando o Dicionário e adicionando alguns termos novos')
for palavra, significado in glossario.items():
    print(f"{palavra.title()}:\n\t{significado}\n")
