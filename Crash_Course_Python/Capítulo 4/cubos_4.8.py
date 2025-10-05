# 4.8 Cubos: 
# Um número elevado à terceira potência é chamado de cubo. 
# Por exemplo, no Python, o cubo de 2 é escrito como "2**3". 
# Escreva uma lista dos primeiros 10 cubos 
# (ou seja, o cubo de cada número inteiro de 1 a 10) 
# e use um loop "for"  para exibir o valor de cada cubo.


cubos = []
for valor in range(1, 11):
    cubo = valor ** 3
    cubos.append(cubo)
print(cubos)