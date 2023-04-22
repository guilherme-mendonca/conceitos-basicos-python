from time import sleep
from random import choice

print("="*15,'\033[35mJokenpô\033[m',"="*15)

jogar = input('\nQuer jogar jekenpô? Digite Sim(s) ou Não(n): ').lower()
if jogar not in ['sim', 'não', 'nao', 'n', 's']:
    print('Erro de digitção, por favor tente novamente.')
    exit()
    
elif jogar in ['nao', 'n'] :
    print('Tudo bem, até a próxima.')
    exit()
            
else:        
    instruncao = input('Deseja ver as instruções de como jogar? Sim(s) ou Não(n)').lower()
    if instruncao in ['s', 'sim']:
        print('''\n\033[35mInstruções de como jogar:\033[m\n
\033[36mO computador vai escolher aleatoriamente pedra, papel ou tesoura. Você também deve
escolher uma dessas opções. Pedra papel ou tesoura. Pedra ganha de tesoura, 
tesoura ganha de papel e papel ganha de tesoura.\033[m\n''')
            
while True:
            
        usuario = input('Digite pedra papel ou tesoura: ')
        if usuario not in ['pedra', 'papel', 'tesoura']: #Se a variável escolha nao estiver em uma das opções do colchete print('')
            print('\033[37mErro de digitação por favor tente novamente.\033[37m')
            continue
                    
        else:
            opcoes = ['pedra', 'papel', 'tesoura']
            computador = (choice(opcoes)) #Escolhe uma das opções dentro da variável.
            print('\033[34mPROCESSANDO...\033[m')
            sleep(2) #O comando sleep faz com que o computador "durma" por um determinado tempo
            
        if computador == usuario:
            print('Empate!')
                
        elif computador == 'pedra' and usuario == 'papel' or computador == 'papel' and usuario == 'tesoura' or computador == 'tesoura' and usuario == 'pedra':
            print(f'\n\033[32mVitória! {usuario} ganha de {computador}\033[m.')
                
        elif computador == 'pedra' and usuario == 'tesoura' or computador == 'tesoura' and usuario == 'papel' or computador == 'papel' and usuario == 'pedra':
            print(f'\n\033[31mDerrota! {computador} ganha de {usuario}\033[m.')
                    
        novo = input('\nDeseja jogar novamente digite Sim(s) ou Não(n).').lower()
        if novo not in ['sim', 'não', 'nao', 'n', 's']:
            print('\033[37mErro de digitação, por favor tente novamente.\033[m')
            break
        
        elif novo in ['sim', 's']:
            continue
            
        else:
            print('Obrigado por jogar!')
            break