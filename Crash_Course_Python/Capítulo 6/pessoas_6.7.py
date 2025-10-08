# 6.7 Pessoas: 
# Comece com o programa escrito para o Exercício 6.1. 
# Crie dois dicionários novos representando pessoas diferentes 
# e armazene todos os três dicionários em uma lista chamada "people". 
# Percorra sua lista de pessoas com um loop. 
# À medida que percorre a lista, exiba tudo o que sabe sobre cada pessoa.


pessoa1 = {
    'nome' : 'erick',
    'sobrenome' : 'cantagallo',
    'idade' : 22,
    'cidade' : 'são paulo',
}
pessoa2 = {
    'nome' : 'ana',
    'sobrenome' : 'silva',
    'idade' : 28,
    'cidade' : 'rio de janeiro',
}
pessoa3 = {
    'nome' : 'carlos',
    'sobrenome' : 'oliveira',
    'idade' : 35,
    'cidade' : 'belo horizonte',
}
pessoas = [pessoa1, pessoa2, pessoa3]
for pessoa in pessoas:
    print(f"Nome: {pessoa['nome'].title()}")
    print(f"Sobrenome: {pessoa['sobrenome'].title()}")
    print(f"Idade: {pessoa['idade']}") #sem o title() porque é dado numérico tipo "int".
    print(f"Cidade: {pessoa['cidade'].title()}")
    print("\n")