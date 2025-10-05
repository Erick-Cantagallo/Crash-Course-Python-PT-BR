# 4.15 Revisão do Código: 
# Escolha três dos programas que você escreveu neste capítulo e 
# modifique cada um deles para atender às recomendações "PEP 8".
#    - Utilize quatro espaços para cada nível de identação. 
#      Configure seu editor de text para inserir quatro espaços sempre que você pressionar a tecla "TAB", 
#      se ainda não tiver configurado (confira o Apêndice B para instruções sobre como fazer isso).
#    - Use menos de 80 caracteres em cada linha e configure seu editor 
#      para mostrar uma linha-guia vertical na posição do 80° caractere.
#    - Não use excessivamente linhas em branco em seus arquivos de programa.

# Como verificar e alterar o espaço do "TAB" no VSCode:
# 1. Vá para "File" > "Preferences" > "Settings" (ou use o atalho Ctrl + ,).
# 2. Na barra de pesquisa, digite "Tab Size".
# 3. Encontre a configuração "Editor: Tab Size" e defina o valor para 4.
# 4. Para garantir que a tecla "TAB" insira espaços em vez do caractere de tabulação, 
# verifique a configuração "Editor: Insert Spaces" e certifique-se de que esteja marcada (ativada).

# Como adicionar uma linha-guia vertical no VSCode:
# 1. Vá para "File" > "Preferences" > "Settings" (ou use o atalho Ctrl + ,).
# 2. Na barra de pesquisa, digite "Rulers".
# 3. Encontre a configuração "Editor: Rulers" e clique em "Edit in settings.json".
# 4. Adicione o valor 80 dentro do array, assim: [80].

# 1. Resposta do exercício 4.13 Buffet
print("Exercício 4.13 Buffet:")
buffet = ("arroz", "feijão", "bife", "salada", "batata frita")
for comida in buffet:
    print(f"- {comida}")
# Tentando modificar um dos elementos (isso causará um erro)
# buffet[0] = "macarrão"  # Descomente esta linha para ver o erro
print("\nMenu reformulado:")
# Reescrevendo a tupla com novas refeições
buffet = ("macarrão", "feijão", "frango grelhado", "salada", "legumes")
for comida in buffet:
    print(f"- {comida}")
print("\n" + "-"*40 + "\n")
# 2. Resposta do exercício 4.14 PEP 8
print("Exercício 4.14 PEP 8:")
print("Consulte o guia de estilo PEP 8 em https://python.org/dev/peps/pep-0008")
print("\n" + "-"*40 + "\n")
# 3. Resposta do exercício 4.15 Revisão do Código
print("Exercício 4.15 Revisão do Código:")
print("Escolha três dos programas que você escreveu neste capítulo e modifique cada um deles para atender às recomendações PEP 8.")
print("Utilize quatro espaços para cada nível de identação, use menos de 80 caracteres por linha e evite linhas em branco excessivas.")
print("Certifique-se de que seu editor de texto está configurado corretamente para essas práticas.")
print("\n" + "-"*40 + "\n")
# Fim das respostas