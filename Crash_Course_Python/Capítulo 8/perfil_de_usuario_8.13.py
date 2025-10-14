# 8.13 Perfil de usuário: 
# Comece com uma cópia do "user_profile.py". 
# Crie um perfil de si mesmo chamado "build_profile()", 
# com seu primeiro nome e sobrenome e três outros pares chave-valor que o representem.

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Erick', 'Cantagallo', #Esse sou eu :) 
                             location='São Paulo',
                             field='Data Science')
print(user_profile)