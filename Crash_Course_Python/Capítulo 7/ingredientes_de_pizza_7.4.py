# 7.4 Ingredientes de pizza: 
# Escreva um loop que solicite ao usuário uma série 
# de ingredientes de pizza até que ele forneça o valor 'quit'. 
# À medida que cada ingrediente é fornecido, 
# exiba uma mensagem informado que esses ingredientes estão sendo adicionados à pizza.


while True:
    ingrediente = input("Informe um ingrediente para adicionar à pizza (ou 'quit' para sair): ")
    if ingrediente.lower() == 'quit':
        print("Finalizando a adição de ingredientes.")
        break
    else:
        print(f"Adicionando {ingrediente} à pizza.")

