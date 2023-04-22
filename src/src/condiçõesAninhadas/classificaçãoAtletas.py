dt = int(input('Digite seu ano de nascimento: '))
idd = 2023 - dt

if idd < 9:
    print(f'O atleta tem {idd} ')
    print('MIRIM')

elif idd < 14:
    print(f'O atleta tem {idd} ')
    print('INFANTIL')

elif idd < 19:
    print(f'O atleta tem {idd} ')
    print('JUNIOR')
    
elif idd < 20:
    print(f'O atleta tem {idd} ')
    print('SÊNIOR')
    
elif idd > 20:
    print(f'O atleta tem {idd} ')
    print('MASTER')