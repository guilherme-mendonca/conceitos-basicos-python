#025                        Verifica se tem santos e Silva no nome
nome = input('Digite seu nome completo: ')
di = nome.upper().split()
print(f'True se o nome ter "SILVA" e False se não tiver. \n {"SILVA" in di}')
print(f'True se o nome ter "SANTOS" no primeiro sobrenome e False se não tiver. \n {"SANTOS" in di[1]}')