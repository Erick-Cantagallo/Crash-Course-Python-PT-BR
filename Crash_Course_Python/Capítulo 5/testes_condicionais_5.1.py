# 5.1 Testes condicionais: 
# Escreva uma série de testes condicionais. 
# Exiba uma afirmação com cada teste descrito e a previsão dos resultados de cada teste. 
# Seu código deve ficar mais ou menos assim:
#
#  car = 'subaru'
#  print("Is car == 'subaru'? I predict True.")
#  print(car == 'subaru')
#
#    Preste bastante atenção ao seus resultados e procure entender por que cada 
#    linha é avaliada como "True" ou "False"
#    Crie, pelo menos, 10 testes. Execute, pelo meos, 
#    5 testes avaliados como "True" e outros 5 avaliados como "False"

# Os testes de condicionais são usados para verificar se uma condição é verdadeira ou falsa.
# Eles são frequentemente usados em estruturas de controle, como if, elif e else, para tomar decisões no código.
# Recomendo dar uma estudada em Lógica Matemática para entender melhor como funcionam os testes condicionais.


# Alguns testes condicionais com previsões de resultados:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
#------------------------------------------------
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#------------------------------------------------
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi') # Lembrando que '!=' significa 'diferente de'.
#------------------------------------------------
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')
#------------------------------------------------
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru') # O método lower() converte todas as letras em minúsculas.
#------------------------------------------------
print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU') # O método upper() converte todas as letras em maiúsculas.
#------------------------------------------------
print("\nIs car.title() == 'Subaru'? I predict True.")
print(car.title() == 'Subaru') # O método title() converte a primeira letra de cada palavra em maiúscula.
#------------------------------------------------
print("\nIs car.startswith('b')? I predict False.")
print(car.startswith('b')) # O método startswith() verifica se a string começa com o caractere especificado.
#------------------------------------------------
print("\nIs car.endswith('u')? I predict True.")
print(car.endswith('u')) # O método endswith() verifica se a string termina com o caractere especificado.
#------------------------------------------------
print("\nIs 'b' in car? I predict True.")
print('b' in car) # O operador 'in' verifica se o caractere especificado está presente na string.
#------------------------------------------------
print("\nIs 'z' in car? I predict False.")
print('z' in car)
#------------------------------------------------
print("\nIs 'a' not in car? I predict False.")
print('a' not in car) # O operador 'not in' verifica se o caractere especificado não está presente na string.
#------------------------------------------------
