#013                      Aumento de salario (porcentagem)

s = float(input('Quanto é o salário?'))
a = float(input('Quanto é o valor de aumento?'))
sn = (((a*s)/100)+s)
print(f'Antes o seu salário era de {s:.2f}, com {a:.0f}% de aumento você passa a receber R${sn:.2f}')