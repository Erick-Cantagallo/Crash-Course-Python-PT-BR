# 7.6 Três saídas: 
# Crie diferentes versões do Exercício 7.4 ou 7.5 
# que executem cada uma das seguintes tarefas, pelo menos uma vez:
#    - Use um teste condicional na instrução "while" para interromper o loop.
#    - Use uma variável "active" para controlar o tempo que o loop é executado.
#    - Use uma instrução "break" para sair do loop quando o usuário inserir o valor "'quit'".


# Caso queira testar cada uma das versões, descomente a seção desejada. 
# Utilize (""") aspas triplas no início e no final para comentar/descomentar blocos de códigos maiores.

# Versão 1: Usando um teste condicional na instrução "while"
print("Versão 1: Usando um teste condicional na instrução 'while'")
while True:
    age = input("Por favor, insira sua idade (ou 'sair' para encerrar): ")
    if age.lower() == 'sair':
        print("Encerrando o programa.")
        break
    else:
        age = int(age)
        if age < 3:
            print("O ingresso é gratuito.")
        elif 3 <= age <= 12:
            print("O ingresso custa US$10.")
        else:
            print("O ingresso custa US$15.")
print("\n")
# Versão 2: Usando uma variável "active" para controlar o loop
print("Versão 2: Usando uma variável 'active' para controlar o loop")
active = True
while active:
    age = input("Por favor, insira sua idade (ou 'sair' para encerrar): ")
    if age.lower() == 'sair':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("O ingresso é gratuito.")
        elif 3 <= age <= 12:
            print("O ingresso custa US$10.")
        else:
            print("O ingresso custa US$15.")
print("\n")
# Versão 3: Usando uma instrução "break" para sair do loop
print("Versão 3: Usando uma instrução 'break' para sair do loop")
while True:
    age = input("Por favor, insira sua idade (ou 'sair' para encerrar): ")
    if age.lower() == 'sair':
        break
    else:
        age = int(age)
        if age < 3:
            print("O ingresso é gratuito.")
        elif 3 <= age <= 12:
            print("O ingresso custa US$10.")
        else:
            print("O ingresso custa US$15.")
print("\n")
print("Obrigado por usar o sistema de ingressos do cinema!")
