#018                        Angulo sen, cos e tan

from math import sin, cos, tan, radians
an = float(input('Qual é o ângulo desejado? '))
sen = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print(f'O valor do seno será {sen:.2f}, o valor de cos {coss:.2f} e o da tangente {tang:.2f}.')