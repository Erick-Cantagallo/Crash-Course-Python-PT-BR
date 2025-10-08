# 7.7 Infinito: 
# Escreva e execute um loop infinito. 
# (Para encerrar o loop, pressione "CTRL+C" ou feche a janela que exibe a saída.)


while True:
    print("Este é um loop infinito. Pressione 'CTRL+C' para sair.")
    # Adicionei uma pausa para evitar que o loop consuma muitos recursos
    import time # Importa o módulo time para usar a função sleep.
    time.sleep(1) # Ele da um tempo de 1 segundo entre as iterações.
    # Remova a linha acima se quiser um loop realmente infinito sem pausas.