# 5.4 Cores de alienígenas #2: 
# Escolha uma cor para um alienígena, 
# como no Exercício 5.3, e escreva uma sequência "if-else".
#    - Se a cor do alienígena for verde, 
#      exiba uma afirmação de que o jogador acabou de ganhar 5 pontos por abrir fogo contra um alienígena.
#    - Se a cor do alienígena for verde, 
#      exiba uma afirmação de que o jogador acabou de ganhar 10 pontos.
#    - Escreva uma versão desse programa 
#      que execute o bloco "if" e outra que execute o bloco "else".


# Essa versão abaixo executa o bloco if garantindo que o alienígena é verde e ganha 5 pontos.
# Logo ele não executa o else.
alien_color = 'green' # Garante que o alienígena é verde.
if alien_color == 'green': # Se for verde ele executa o bloco if (logo ele nunca executa o else).
    print("Você ganhou 5 pontos por abrir fogo contra um alienígena verde.")
else:
    print("Você ganhou 10 pontos por abrir fogo contra um alienígena que não é verde.")
#------------------------------------------------------------------------------
# Essa versão abaixo executa o bloco else garantindo que o alienígena não é verde e ganha 10 pontos.
# Logo ele não executa o if.
alien_color = 'red' # Garante que o alienígena não é verde.
if alien_color == 'green': # Se fosse verde ele executaria o bloco if, mas como não é ele executa o else.
    print("Você ganhou 5 pontos por abrir fogo contra um alienígena verde.")
else:
    print("Você ganhou 10 pontos por abrir fogo contra um alienígena que não é verde.")
