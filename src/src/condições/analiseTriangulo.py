r1 = float(input('Digite o comprimento da primeira reta em cm '))
r2 = float(input('Digite o comprimento da segunda reta em cm '))
r3 = float(input('Digite o comprimento da terceira reta em cm '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3+r1 > r2:
    print('Essas retas PODEM formar um triângulo.')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')