# 5.5 Cores alienígenas #3: 
# Converta sua sequência "if-else" do Exercício 5.4 em uma sequência "if-elif-else".
#    - Se o alienígena for verde, 
#      exiba uma afirmação de que o jogador ganhou 5 pontos.
#    - Se o alienígena for amarelo, 
#      exiba uma afirmação de que o jogador ganhhou 10 pontos.
#    - Se o alienígena for vermelho, 
#      exiba uma afirmação de que o jogador ganhou 15 pontos.
#    - Escreva três versões desse programa, 
#      assegurando que cada afirmação exibida seja correspondente à cor adequada do alienígena.


#------------------------------------------------------------------------------
# Essa versão abaixo executa o bloco if garantindo que o alienígena é verde e ganha 5 pontos.
# Logo ele não executa o elif e o else.
alien_color = 'green' # Garante que o alienígena é verde.
if alien_color == 'green': # Se for verde ele executa o bloco if (logo ele nunca executa o elif e o else).
    print("Você ganhou 5 pontos por abrir fogo contra um alienígena verde.")
elif alien_color == 'yellow': # Nunca executa esse bloco.
    print("Você ganhou 10 pontos por abrir fogo contra um alienígena amarelo.")
else: # Nunca executa esse bloco.
    print("Você ganhou 15 pontos por abrir fogo contra um alienígena vermelho.")
#------------------------------------------------------------------------------
# Essa versão abaixo executa o bloco elif garantindo que o alienígena é amarelo e ganha 10 pontos.
# Logo ele não executa o if e o else.
alien_color = 'yellow' # Garante que o alienígena é amarelo.
if alien_color == 'green': # Nunca executa esse bloco.
    print("Você ganhou 5 pontos por abrir fogo contra um alienígena verde.")
elif alien_color == 'yellow': # Se for amarelo ele executa o bloco elif (logo ele nunca executa o if e o else).
    print("Você ganhou 10 pontos por abrir fogo contra um alienígena amarelo.")
else: # Nunca executa esse bloco.
    print("Você ganhou 15 pontos por abrir fogo contra um alienígena vermelho.")
#------------------------------------------------------------------------------
# Essa versão abaixo executa o bloco else garantindo que o alienígena é vermelho e ganha 15 pontos.
# Logo ele não executa o if e o elif.
alien_color = 'red' # Garante que o alienígena é vermelho.
if alien_color == 'green': # Nunca executa esse bloco.
    print("Você ganhou 5 pontos por abrir fogo contra um alienígena verde.")
elif alien_color == 'yellow': # Nunca executa esse bloco.
    print("Você ganhou 10 pontos por abrir fogo contra um alienígena amarelo.")
else: # Se for vermelho ele executa o bloco else (logo ele nunca executa o if e o elif).
    print("Você ganhou 15 pontos por abrir fogo contra um alienígena vermelho.")
#------------------------------------------------------------------------------
