p = float(input('Digite o preço das compras: '))

print('''Formas de pagamento digite:
1 - dinehiro e cheque
2 - à vista cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')
fp = int(input('Qual será a forma de pagamento? '))

if fp == 1:
    print(f'Opcão escolhida: dinheiro/cheque com 10% de desconto. Você irá pagar R${p-(p*0.1):.2f}.') #Primeiro calculamos quanto é a porcentagem do preço e subtraímos ao própio preço
    
elif fp == 2:
    print(f'Opcão escolhida: à vista no cartão com 5% de desconto. Você irá pagar R${p-(p*0.5):.2f}.') 
    
elif fp == 3:
    print(f'Opcão escolhida: 2x no cartão. Você irá pagar 2x R${p:.2f}.')
    
elif fp == 4:
    pl = int(input('Digite o número de parcelas: '))
    print(f'Opcão escolhida: 3x no cartão com 20% de juros. Parcelado em 10x de {p/pl:.2f} Você irá pagar R${p+(p*0.2):.2f}.')