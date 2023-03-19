s = float(input('Digite o salário do funcionário R$ '))
if s > 1250.00:
    p = '10%'
    a = s+(0.1*s)
else:
    p = '15%'
    a = s+(0.15*s)
print(f'O aumento será de {p}, seu novo salário será de R$ {a:.2f} ')