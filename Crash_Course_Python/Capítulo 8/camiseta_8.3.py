# 8.3 Camiseta: 
# Crie uma função chamada make_shirt() 
# que aceita um tamanho e o texto que deve ser estampado na camiseta. 
# A função deve exibir uma frase resumindo o tamanho da camiseta e a mensagem estampada nela.


def make_shirt(size, message):
    print(f"A camiseta é tamanho {size} e tem a mensagem: '{message}' estampada nela.")
make_shirt('M', 'Python é incrível!')
make_shirt('G', 'Eu amo programação!')
make_shirt(size='P', message='Camiseta personalizada!') # Para demonstrar o uso de argumentos nomeados.
# Chame a função para fazer uma camiseta de tamanho médio com a mensagem "Python é incrível!".
# Em seguida, chame a função novamente para fazer uma camiseta de qualquer tamanho, 
# mas com uma mensagem diferente.