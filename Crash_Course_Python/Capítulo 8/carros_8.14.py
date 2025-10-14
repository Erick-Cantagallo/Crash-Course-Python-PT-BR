# 8.14 Carros: 
# Crie uma função que armazena informações sobre um carro em um dicionário. 
# A função deve sempre receber um fabricante e um nome de modelo. 
# Em seguida, deve aceitar um número arbitrário de argumentos nomeados. 
# Chame a função com as informações necessárias e os dois outros pares nome-valor, 
# como uma cor ou um recurso opcional. 
# Sua função deve funcionar mais ou menos assim:
# car = make_car('subaru', 'outback', color='blue', tow_package=True). 
# Exiba o dicionário retornado para garantir que todas as informações foram corretamente armazenadas.


def make_car(fabricante, modelo, **informacoes_adicionais):
    carro = {
        'fabricante': fabricante,
        'modelo': modelo
            }
    
    for chave, valor in informacoes_adicionais.items():
        carro[chave] = valor
    return carro
meu_carro = make_car('subaru', 'outback', cor='azul', pacote_reboque=True)
print(meu_carro)
meu_carro2 = make_car('honda', 'civic', cor='preto', ano=2020)
print(meu_carro2)
meu_carro3 = make_car('ford', 'mustang', cor='vermelho', motor='V8', ano=2021)
print(meu_carro3)
meu_carro4 = make_car('chevrolet', 'camaro', cor='amarelo', motor='V6', ano=2022, transmissao='manual')
print(meu_carro4)
meu_carro5 = make_car('toyota', 'corolla', cor='branco', ano=2019, pacote_seguranca=True)
print(meu_carro5)

