#                                           Dobro, triplo e raiz
from math import sqrt, floor          #quando importamos toda a biblioteca precisamos cita-la antes da #função difrente se inportamos uma função especifica como visto no codigo
n = float(input('Digite um valor: '))
d = n * 2
t = n * 3
num = int(input('Digite um número:'))
raiz = sqrt(num)
print(f'A raiz de {num} é {floor(raiz)}')