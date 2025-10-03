# 3.8 Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de conhecer.
#    - Armazene esses locais em uma lista. Verifique se ela não esta em ordem alfabética.
#    - Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente;
#      basta exibi-la como uma lista crua do Python.
#    - Use "sorted()" para exibir sua lista em ordem alfabética, sem alterar a lista original.
#    - Mostre que sua lista ainda está na ordem original exibindo-a.
#    - Use o "sorted()" para exibir sua lista em ordem alfabética reversa,
#      sem alterar a ordem original dela.
#    - Use o "reverse()" para alterar a ordem de sua lista. 
#      Exiba essa lista para mostrar que sua ordem foi alterada.
#    - Use o "reverse()" para alterar a ordem de sua lista novamente. 
#      Exiba-a a fim de mostrar que voltou à ordem original.
#    - Use o "sort()" para alterar sua lista para que ela seja armazenada em ordem alfabética inversa. 
#      Exiba a lista para mostrar que sua ordem foi alterada.
#    - Use "sort()" para alterar sua lista, de modo que ela seja armazenada em ordem alfabética inversa. 
#      Exiba a lista para mostrar que sua ordem foi alterada.


lugares = ['Japão', 'Itália', 'Nova Zelândia', 'Grécia', 'Turquia']
#---------------
print("Lista original:")
print(lugares)
#---------------
print("\nLista em ordem alfabética:")
print(sorted(lugares))
#---------------
print("\nLista original novamente:")
print(lugares)
#---------------
print("\nLista em ordem alfabética reversa:")
print(sorted(lugares, reverse=True))
#---------------
print("\nInvertendo a ordem da lista original:")
lugares.reverse()
print(lugares)
#---------------
print("\nInvertendo novamente para a ordem original:")
lugares.reverse()
print(lugares)
#---------------
print("\nOrdenando a lista em ordem alfabética:")
lugares.sort()
print(lugares)
#---------------
print("\nOrdenando a lista em ordem alfabética reversa:")
lugares.sort(reverse=True)
print(lugares)
#---------------