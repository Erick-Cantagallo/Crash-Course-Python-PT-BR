# 7.8 Lanchonete: 
# Crie uma lista "sandwich_orders" e a preencha com o nome de diversos sanduíches. 
# Depois, crie uma lista vazia chamada "finished_sandwiches". 
# Percorra a lista de pedidos de sanduíches com um loop 
# e exiba uma mensagem para cada pedido, 
# como: ""Seu lanche de atum" está pronto". 
# Conforme cada sanduíche é preparado, passe-os para a lista de sanduíches prontos. 
# Após todos os sanduíches terem sido preparados, 
# exiba uma mensagem enumerando cada um deles.


sandwich_orders = ['atum', 'frango', 'carne', 'bacon', 'ovo']
finished_sandwiches = []

# Loop para processar os pedidos
print("Processando pedidos...")
while sandwich_orders:
    # Retira o último pedido da lista (LIFO) = significa Last-In, First-Out (em português, "Último a Entrar, Primeiro a Sair")
    current_sandwich = sandwich_orders.pop() # Pega a lista principal e retira o último item dela.
    # Simula a preparação do sanduíche (com uma mensagem)
    
    print(f"Seu lanche de {current_sandwich} está pronto.")
    
    # Move o sanduíche pronto para a lista de finalizados
    finished_sandwiches.append(current_sandwich)

# Impressão final após o loop terminar (todos os sanduíches prontos)
print("\nTodos os pedidos foram processados.")
print("Lanches prontos:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
