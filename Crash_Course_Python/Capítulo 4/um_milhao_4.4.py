# 4.4 Um milhão: 
# Crie uma lista com números de um a um milhão e,
# em seguida, utilize um loop "for" para exibi-los. 
# (Se a saída estiver demorando muito, interrompa-a 
# pressionando "CTRL+C" ou fechando a janela de saída.)


numeros = list(range(1, 1000001)) # Cria uma lista de números de 1 a 1.000.000
for numero in numeros:
    print(numero)