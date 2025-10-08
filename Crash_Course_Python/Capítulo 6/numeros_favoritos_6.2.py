# 6.2 Números favoritos: 
# Use um dicionário para armazenar os números favoritos das pessoas. 
# Pense em cinco nomes e os utilize como chaves em seu dicionário. 
# Pense em um número favorito para cada pessoa e armazene cada um como um valor em seu dicionário. 
# Exiba o nome de cada pessoa e seu número favorito. 
# Para que tudo fique ainda mais divertido, 
# pergunte a alguns amigos e obtenha alguns dados reais para o seu programa.


numeros_favoritos = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 3,
    'Diana': 8,
    'Eve': 13
}

for nome, numero in numeros_favoritos.items():
    print(f"O número favorito do(a) {nome} é {numero}.")
