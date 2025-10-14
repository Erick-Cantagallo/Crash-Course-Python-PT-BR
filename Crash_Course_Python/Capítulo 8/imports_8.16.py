# 8.16 Imports: 
# Usando um programa que você escreveu e que tenha apenas uma função, 
# armazene essa função em um arquivo separado. 
# Importe a função para o arquivo de programa principal 
# e chame a função usando cada uma dessas abordagens:

#  import nome_módulo
#  from nome_módulo import nome_função
#  from nome_módulo import nome_função as nf
#  import nome_módulo as nm
#  from nome_módulo import *

# ----------------------------------------------------------------------
# 1. import nome_módulo (Importa o módulo inteiro)
# Usar o prefixo do módulo (car_functions) para chamar a função.
# ----------------------------------------------------------------------
import car_functions

print("\n--- Teste 1: import nome_módulo ---")
carro1 = car_functions.make_car('toyota', 'corolla', cor='branco')
print(carro1)

# ----------------------------------------------------------------------
# 2. from nome_módulo import nome_função (Importa apenas a função)
# Chamar a função diretamente, sem prefixo.
# ----------------------------------------------------------------------
from car_functions import make_car

print("\n--- Teste 2: from nome_módulo import nome_função ---")
carro2 = make_car('honda', 'civic', ano=2022)
print(carro2)

# ----------------------------------------------------------------------
# 3. from nome_módulo import nome_função as nf (Importa com um alias)
# Usar o alias (mc) para chamar a função.
# ----------------------------------------------------------------------
from car_functions import make_car as mc

print("\n--- Teste 3: from nome_módulo import nome_função as nf (mc) ---")
carro3 = mc('ford', 'mustang', motor='v8')
print(carro3)

# ----------------------------------------------------------------------
# 4. import nome_módulo as nm (Importa o módulo inteiro com um alias)
# Usar o alias (cf) seguido do nome da função.
# ----------------------------------------------------------------------
import car_functions as cf

print("\n--- Teste 4: import nome_módulo as nm (cf) ---")
carro4 = cf.make_car('chevrolet', 'camaro', cor='amarelo')
print(carro4)

# ----------------------------------------------------------------------
# 5. from nome_módulo import * (Importa tudo diretamente, sem prefixo)
# Geralmente evitado, pois pode causar conflitos de nomes.
# ----------------------------------------------------------------------
from car_functions import *

print("\n--- Teste 5: from nome_módulo import * ---")
carro5 = make_car('tesla', 'model 3', piloto_automatico=True)
print(carro5)