nome = input('Digite seu nome completo: ')
nome = nome.upper().split()
primeiro_nome = nome[0]
ultimo_nome = nome[-1]
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')