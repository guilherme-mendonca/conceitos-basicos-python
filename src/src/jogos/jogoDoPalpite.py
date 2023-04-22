from random import randint
from time import sleep

#text        background
 
#30   black    preto    40
#31   red      vermelho 41
#32   green    verde    42
#33   yellow   amarelo  43
#34   blue     azul     44
#35   magenta  Magenta  45
#36   cyan     ciano    46
#37   grey     cinza    47
#97   white    branco   07

#Para colocar cores e estilos no seu codigo utilize o ANSI '\033[style;text;backm e no final \033[m'     
   
print('='*28,'Jogo do Palpite','='*28)
jogar = (input('\nQuer jogar um jogo? Digite SIM(s) ou NÃO(n): ')).lower()

while True: #Inicia um loop. Se a variável novo for igual a sim
    if jogar not in ['sim', 's', 'n', 'nao', 'não']: #O operador 'not in' verifica se determinado valor esta ausente em uma sequencia
        print('Erro, por favor reinicie o programa')
        break #Break para o programa
    
    if jogar == 'n' or jogar == 'nao' or jogar == 'não':#Se o valor de jogar for igual n, não ou nao roda print
        print('Tudo bem, até a proxima!')
        break
    
    if jogar == 'sim' or 's':  #Se jogar for igual a sim entao o jogo inicia
        print('\033[35m=\033[m'*60)
        print('\033[33mIrei pensar em um número entre 0 e 5 e você irá tentar adivinha-lo.\033[m')#33 representa a cor amarela no codigo ANSI
        print('\033[35m=\033[m'*60)
        
        num = int(randint(0,5)) # Usando o metodo randint faz a maquina 'pensar' em um um número
        p = int(input('\033[33mQual foi o número pensado entre 0 e 5?\033[33m\n'))#jogador tenta adivinhar
        
        print('\033[34mPROCESSANDO...\033[34m')
        sleep(2) #O comando sleep faz com que o computador "durma" por alguns segundos
        
        
    if p == num:    #Se o número digitado for igual ao pensado voce ganhou 
        print('\033[1;32mUoou, você acertou o número PARABÉNS!\033[m\n') 
    else: #Se o número digitado nao for igual ao pensado voce perdeu
        print(f'\33[1;31mHehehe, você errou! Eu pensei no número {num}\033[m.\n')
    
    novo = input('Quer jogar novamente digite "sim(s)" ou "não(n)" ').lower() #Pergunta se o usuario quer jogar novamente e coloca a reposta dele em minuscula
    
    if novo not in ['sim', 's', 'n', 'não', 'nao']: #Se o valor de novo estiver na sequência o programa dá erro
        print('Erro, por favor reinicie o programa!')
        break #Break para o programa
    
    if novo not in ['sim', 's']: #Se o valor de novo estiver ausente na sequancia entao o programa para de rodar
        print('Tudo bem meu chapa, até a próxima.')
        break
    else:
        continue #Continue, o prgrama continua rodar no loop