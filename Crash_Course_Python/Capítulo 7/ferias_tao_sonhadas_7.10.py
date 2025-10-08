# 7.10 Férias tão sonhadas: 
# Crie uma pesquisa que pergunte aos usuários sobre as férias de seus sonhos. 
# Crie um prompt mais ou menos assim: 
# "Se pudesse visitar qualquer lugar do mundo, para onde iria ?". 
# Inclua um bloco de códigos que exiba os resultados dessa pesquisa.


respostas = {}
perguntas = "Se pudesse visitar qualquer lugar do mundo, para onde iria ?\n"
perguntas += "(Digite 'sair' para encerrar a pesquisa)\n"
while True:
    nome = input("Qual o seu nome? ('sair') ")
    if nome.lower() == 'sair':
        break
    resposta = input(perguntas)
    if resposta.lower() == 'sair':
        break
    respostas[nome] = resposta
    print(f"Obrigado por participar da pesquisa, {nome}!")
print("\n--- Resultados da Pesquisa ---")
for nome, resposta in respostas.items():
    print(f"{nome} gostaria de visitar {resposta}.")

