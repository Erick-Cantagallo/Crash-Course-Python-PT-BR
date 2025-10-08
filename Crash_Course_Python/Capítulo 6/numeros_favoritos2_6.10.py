# 6.10 Números favoritos:
# Modifique seu programa do Exercício 6.2 
# para que cada pessoa possa ter mais de um número favorito. 
# Depois, exiba o nome de cada pessoa com seus números favoritos.

# 6.2 Números favoritos:
numeros_favoritos = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 3,
    'Diana': 8,
    'Eve': 13
}
# Modificação para permitir múltiplos números favoritos:
numeros_favoritos = {
    'Alice': [7, 11],
    'Bob': [42, 1],
    'Charlie': [3, 9, 27],
    'Diana': [8],
    'Eve': [13, 21]
}
for nome, numeros in numeros_favoritos.items():
    numeros_formatados = ', '.join(str(num) for num in numeros) # Esse ".join" tem a função de   | O "str(num)" tem a funçao de
                                                                # formatar a lista em uma string | transformar cada número em 
                                                                # separada por vírgulas.         | string.
    print(f"O(s) número(s) favorito(s) do(a) {nome} é(são): {numeros_formatados}.")
