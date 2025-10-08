# 6.6 Pesquisa:
# Use o código de "favorite_languages.py".
#    - Crie uma lista de pessoas que deveriam participar da pesquisa de linguagem favoritas. 
#      Inclua alguns nomes que já estão no dicionário e outros que não estão.
#    - Percorra com um loop a lista de pessoas que devem participar da pesquisa. 
#      Se já tiveram respondido, exiba uma mensagem agradecendo a resposta. 
#      Se ainda não tiverem respondido, exiba uma mensagem as convidando a participar.


favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

pessoas_para_pesquisar = ['jen', 'sarah', 'maria', 'carlos', 'edward', 'ana']

for pessoa in pessoas_para_pesquisar:
    if pessoa in favorite_languages.keys():
        print(f'Obrigado por responder a pesquisa, {pessoa.title()}!')
    else:
        print(f'Olá {pessoa.title()}, por favor, participe da nossa pesquisa de linguagem favorita!')
    print()

print(favorite_languages.values()) #para visualizar as linguagens favoritas cadastradas.
