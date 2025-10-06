# 5.11 Números ordinais: 
# Os números ordinais designam sua posição em uma lista, 
# como 1° ou 2°. Em inglês, 1st ou 2nd. 
# A maioria dos números ordinais em inglês termina th, exceto 1,2 e 3.
#    - Armazene os números de 1 a 9 em uma lista.
#    - Percorra com um loop a lista.
#    - Use uma sequência "if-elif-else" dentro do loop para exibir a 
#      terminação ordinal adequada para cada número. 
#      Sua saída deve ler "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", 
#      e cada resultado deve estar em uma linha separada.


numeros = list(range(1, 10))
for numero in numeros:
    if numero == 1:
        print(f"{numero}st")
    elif numero == 2:
        print(f"{numero}nd")
    elif numero == 3:
        print(f"{numero}rd")
    else:
        print(f"{numero}th")