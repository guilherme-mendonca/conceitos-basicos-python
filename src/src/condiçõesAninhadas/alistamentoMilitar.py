dt = int(input('Digite seu ano de nascimento: '))
idd = 2023 - dt

if idd < 18:
    print(f'Você ainda vai se alistar para o exécito.')
    if 18-idd == 1:
        print(f'Falta {18-idd} ano para você se alistar.')
    elif 18-idd != 1:
        print(f'Falta {18-idd} anos para você se alistar.')

elif idd > 18:
    print(f'Já passou {idd-18} anos do tempo de alistamento.')

elif idd == 18:
    print(f'Está na hora de você se alistar para o exécito.')
    