# 5.2 Mais testes condicionais: 
# Não é necessário restringir o número de testes a 10. 
# Caso queira executar mais comparações, escreva mais testes e os adicione a "conditional_tests.py". 
# Gere, pelo menos, um resultado "True" e um "False" para cada condição a seguir:
#    - Testes com operador de igualdade e de diferença com strings.
#    - Testes usando o método "lower()".
#    - Testes numéricos com operadores de "igualdade"("=") e de "diferença"("!="), 
#      "maior e menor que"(">","and","<"), "maior ou igual que"(">","or","=") 
#       e "menor ou igual a"("<","or","=").

# Os testes de condicionais são usados para verificar se uma condição é verdadeira ou falsa.


print("\n=== Testes com método lower() ===")
print(f'"hello".lower() == "hello" → { "hello".lower() == "hello" }')
print(f'"hello".lower() == "Hello" → { "hello".lower() == "Hello" }')
print(f'"Python".lower() == "python" → { "Python".lower() == "python" }')
print(f'"Python".lower() == "Python" → { "Python".lower() == "Python" }')
#----------------------------------------------------------------------------------
print("\n=== Testes de igualdade e diferença com strings ===")
print(f'"world" == "world" → { "world" == "world" }')
print(f'"world" != "World" → { "world" != "World" }')
#----------------------------------------------------------------------------------
print("\n=== Testes lexicográficos (ordem alfabética de strings) ===")
print(f'"Python" > "Java" → { "Python" > "Java" }')
print(f'"Java" < "Python" → { "Java" < "Python" }')
print(f'"Python" >= "Python" → { "Python" >= "Python" }')
print(f'"Java" <= "Java" → { "Java" <= "Java" }')
#----------------------------------------------------------------------------------
print("\n=== Testes compostos com strings ===")
print(f'("hello" == "hello" and "world" == "world") → { "hello" == "hello" and "world" == "world" }')
print(f'("hello" == "hello" or "world" == "World") → { "hello" == "hello" or "world" == "World" }')
#----------------------------------------------------------------------------------
print("\n=== Testes numéricos ===")
print(f'42 == 42 → { 42 == 42 }')
print(f'42 != 43 → { 42 != 43 }')
print(f'42 > 41 → { 42 > 41 }')
print(f'42 < 43 → { 42 < 43 }')
print(f'42 >= 42 → { 42 >= 42 }')
print(f'42 <= 43 → { 42 <= 43 }')
#----------------------------------------------------------------------------------
print("\n=== Testes compostos com números ===")
print(f'(42 > 40 and 42 < 45) → { 42 > 40 and 42 < 45 }')
print(f'(42 >= 40 or 42 <= 41) → { 42 >= 40 or 42 <= 41 }')
