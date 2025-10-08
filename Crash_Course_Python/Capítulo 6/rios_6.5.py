# 6.5 Rios:
# Crie um dicionário contendo os três principais rios e o país por onde cada rio passa. 
# Um par chave-valor pode ser "nile" : "egypt"
#    - Use um loop para exibir uma frase sobre cada rio, como: "O nilo atravessa o Egito."
#    - Use um loop para exibir o nome de cada rio incluído no dicionário.
#    - Use um loop para exibir o nome de cada país incluído no dicionário.


rios = {'Nilo' : 'Egito',
        'Amazonas' : 'Brasil',
        'Yangtzé' : 'China'}

for rio, pais in rios.items():
    print(f'O {rio} atravessa o {pais}.')
print()
for rio in rios.keys():
    print(rio)
print()
for pais in rios.values():
        print(pais)
print()