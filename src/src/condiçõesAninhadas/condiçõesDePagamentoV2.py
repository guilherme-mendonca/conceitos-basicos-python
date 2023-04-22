p = float(input('Digite o preço das compras: '))

while True: #Cria  um loop, ele é iniciado se a variável v for diferente de 'ok' 
    print('''Formas de pagamento digite:
    1 - dinehiro e cheque
    2 - à vista cartão
    3 - 2x no cartão
    4 - 3x ou mais no cartão''')
    fp = int(input('Qual será a forma de pagamento? '))

    if fp == 1:
        print(f'Opcão escolhida: dinheiro/cheque com 10% de desconto. Você irá pagar R${p-(p*0.1):.2f}.') #Primeiro calculamos quanto é a porcentagem do preço e subtraímos ao própio preço
        v = input('Digite "ok" para efetuar a compra ou "cancelar" para escolher outra forma de pagamento: ').lower()
        if v == 'ok':   #Verifica se a variavel v é igual a 'ok' entao print('Compra efetuada...')senão continue,volta o programa para o começo.
            if v != 'ok': #Verifica se v é diferente de 'ok' então print('Erro') e para o programa.
                print('Erro, digite novamente.')
                break
            
            print('Compra efetuada com sucesso!')
            break    
        else:
            continue
        
    elif fp == 2:
        print(f'Opcão escolhida: à vista no cartão com 5% de desconto. Você irá pagar R${p-(p*0.5):.2f}.') 
        v = input('Digite "ok" para efetuar a compra ou "cancelar" para escolher outra forma de pagamento: ').lower()
        if v == 'ok':
            if v != 'ok': 
                print('Erro, digite novamente.')
                break
            
            
            print('Compra efetuada com sucesso!')
            break
        else:
            continue
        
    elif fp == 3:
        print(f'Opcão escolhida: 2x no cartão. Você irá pagar 2x R${p:.2f}.')
        v = input('Digite "ok" para efetuar a compra ou "cancelar" para escolher outra forma de pagamento: ').lower()
        if v == 'ok':
            if v != 'ok': 
                print('Erro, digite novamente.')
                break
            
            print('Compra efetuada com sucesso!')
            break    
        else:
            continue

    elif fp == 4:
        pl = int(input('Digite o número de parcelas: '))
        print(f'Opcão escolhida: 3x no cartão com 20% de juros. Parcelado em 10x de {p/pl:.2f} Você irá pagar R${p+(p*0.2):.2f}.')
        v = input('Digite "ok" para efetuar a compra ou "cancelar" para escolher outra forma de pagamento: ').lower()
        if v == 'ok':
            if v != 'ok': 
                print('Erro, digite novamente.')
                break
            
            print('Compra efetuada com sucesso!')
            break    
        else:
            continue