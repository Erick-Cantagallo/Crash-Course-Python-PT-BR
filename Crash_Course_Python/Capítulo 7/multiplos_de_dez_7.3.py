# 7.3 Múltiplos de dez: 
# Solicite ao usuário um número e informe se o número é múltiplo de 10 ou não.


numero = int(input("Digite um número: "))
if numero % 10 == 0:
    print(f"O número {numero} é múltiplo de 10.")
else:
    print(f"O número {numero} não é múltiplo de 10.")

