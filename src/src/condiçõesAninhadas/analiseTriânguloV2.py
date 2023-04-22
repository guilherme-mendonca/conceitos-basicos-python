r1 = float(input('Digite o comprimento da primeira reta em (cm): '))
r2 = float(input('Digite o comprimento da segunda reta em (cm): '))
r3 = float(input('Digite o comprimento da terceira reta (cm): '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3+r1 > r2:
    print('Essas retas PODEM formar um triângulo.')
    
    if r1 == r2 == r3:
        print('Esse triangulo é Equilátero')
    
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('Esse triângulo é Isósceles')
    
    elif r1 != r2 or r1 != r3:
        print('Esse triângulo é Escaleno')

else:
    print('Essas retas NÃO PODEM formar um triângulo.')
