# 8.15 Imprimindo modelos("printing_models.py"): 
# Insira as funções do exemplo "printing_models.py" em um arquivo separado 
# chamado "printing_functions.py". 
# Escreva uma instrução "import" na parte superior do "printing_models.py" 
# e modifique o arquivo para usar as funções importadas.



# Linha de importação
import printing_functions as pf

# Dados
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Chamada das funções importadas
# Usamos o alias (pf) seguido do nome da função
pf.print_models(unprinted_designs, completed_models) 
pf.show_completed_models(completed_models)

# Opcional: Provar que a lista original está vazia
print(f"\nLista de designs não impressos após a execução: {unprinted_designs}")