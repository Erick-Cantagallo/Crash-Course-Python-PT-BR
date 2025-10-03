# 3.10 Funções: Pense em coisas que você conseguiria armazenar em uma lista. 
# Por exemplo, você pode criar uma lista de montanhas, rios, países, cidades,
# idiomas ou qualquer outra coisa que quiser. 
# Crie um programa com uma lista contendo esses itens e, em seguida,
# use cada função apresentada nesse capítulo, pelo menos, uma vez.


#---------------------------------------
lugares = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia']
print("Lista original:", lugares)
#---------------------------------------
print("Lista em ordem alfabética:", sorted(lugares))
print("Lista original após sorted():", lugares)
#---------------------------------------
print("Lista em ordem alfabética reversa:", sorted(lugares, reverse=True))
#---------------------------------------
lugares.reverse()
print("Lista após reverse():", lugares)
#---------------------------------------
lugares.reverse()
print("Lista após reverter novamente:", lugares)
#---------------------------------------
lugares.sort()
print("Lista após sort():", lugares)
#---------------------------------------
lugares.sort(reverse=True)
print("Lista após sort() em ordem reversa:", lugares)
#---------------------------------------
print("Número de lugares na lista:", len(lugares))
#---------------------------------------
# Adicionando um novo lugar
lugares.append('Equador')
print("Lista após append():", lugares)
#---------------------------------------
# Inserindo um lugar no início
lugares.insert(0, 'Venezuela')
print("Lista após insert() no início:", lugares)
#---------------------------------------
# Removendo um lugar
removido = lugares.pop()
print(f"Lista após pop() removendo {removido}:", lugares)
#---------------------------------------
# Removendo um lugar específico
lugares.remove('Chile')
print("Lista após remove() de 'Chile':", lugares)
#---------------------------------------
# Deletando um lugar pelo índice
del lugares[1]
print("Lista após del do índice 1:", lugares)
#---------------------------------------
# Limpando a lista
lugares.clear()
print("Lista após clear():", lugares)