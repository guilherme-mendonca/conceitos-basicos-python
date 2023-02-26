#023                Unidade dos números
num = str(input('Digite um número de 0 a 9999: '))
di = num.split()
print(f'Unidade: {(di[0] [3])}')
print(f'Dezena: {(di[0] [2])}')
print(f'Centena: {(di[0] [1])}')
print(f'Milhar: {(di[0] [0])}')