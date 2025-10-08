# 7.2 Reservas em restaurante: 
# Crie um programa que pergunte quantos lugares em uma mesa o usuário precisa. 
# Se a resposta for mais de oito, 
# exiba uma mensagem informando que é necessário aguardar por uma mesa. 
# Caso contrário, informe que a mesa já está disponível.


lugares = int(input("Quantos lugares você precisa para a mesa? "))
if lugares > 8: 
    print("Você terá que aguardar por uma mesa.")
else:  #Só entra na condição else se for maior que 8
    print("Sua mesa já está disponível.")
