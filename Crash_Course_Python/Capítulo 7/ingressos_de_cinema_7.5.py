# 7.5 Ingressos de cinema: 
# Um cinema cobra preços de ingressos diferentes, 
# dependendo da idade da pessoa. Se a pessoa for menor de 3 anos, 
# o ingresso é gratuito; se tiver entre 3 e 12 anos, 
# o ingresso custa US$10; e caso tenha mais de 12 anos, 
# o ingresso custa US$15. 
# Escreva um loop que pergunte a idade dos usuários e, 
# em seguida, informe o preço do ingresso do cinema.


while True:
    idade = input("Por favor, insira sua idade (ou 'sair' para encerrar): ")
    if idade.lower() == 'sair':
        break
    idade = int(idade)
    if idade < 3:
        preco = 0
    elif 3 <= idade <= 12:
        preco = 10
    else:
        preco = 15
    print(f"O preço do ingresso é: R${preco}")
