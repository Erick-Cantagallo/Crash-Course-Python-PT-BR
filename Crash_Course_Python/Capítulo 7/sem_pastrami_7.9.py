# 7.9 Sem pastrami: 
# Usando a lista "sandwich_orders" do Exercício 7.8, 
# assegure-se de que o sanduíche "pastrami" apareça na lista pelo menos três vezes. 
# Faça mais um que a lanchonete está sem pastrami e, em seguida, 
# use um loop "while" para remover todas as ocorrência de "pastrami" em "sandwich_orders". 
# Faça questão de que nenhum sanduíche de pastrami acabe em "finished_sandwiches".


sandwich_orders = ['atum', 'pastrami', 'frango', 'pastrami', 'bacon', 'ovo', 'pastrami']
finished_sandwiches = []
print("A lanchonete está sem pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Seu lanche de {current_sandwich} está pronto.")
    finished_sandwiches.append(current_sandwich)


