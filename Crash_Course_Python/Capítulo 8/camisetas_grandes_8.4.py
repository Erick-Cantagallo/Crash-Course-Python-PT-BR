# 8.4 Camisetas grandes: 
# Modifique a função "make_shirt()" 
# para que as camisetas sejam grandes por padrão 
# com a seguinte frase estampada: "Eu amo Python". 
# Escreva uma camiseta grande e uma média com a mensagem padrão 
# e uma camiseta de qualquer tamanho com uma frase diferente.


def make_shirt(size='G', message='Eu amo Python'): # Isso deixa os parâmetros com valores padrão.
    print(f"A camiseta é tamanho {size} e tem a mensagem: '{message}' estampada nela.")
make_shirt()  # Camiseta grande com mensagem padrão.
make_shirt('M')  # Camiseta média com mensagem padrão.
make_shirt(size='P', message='Camiseta personalizada!') # Camiseta pequena com mensagem personalizada.