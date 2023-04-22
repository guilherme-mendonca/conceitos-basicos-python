val = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual é o seu salário? R$'))
an = int(input('Em quantos anos será pago? '))
prest = val / (an * 12)
porcenSal = sal * 0.3
print(f'Voçe terá que pagar R${prest:.2f} em {an} ano(s).')

if  prest >= porcenSal:
    print(f'Empréstimo negado, você não o valor da prestação deve ser menor que 30% de seu salário.')

else:    
    print(f'Empréstimo aprovado!')