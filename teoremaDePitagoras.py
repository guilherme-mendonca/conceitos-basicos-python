#017                    Pitágoras
import math
co = float(input('Qual é o comprimento do cateto oposto em metros?'))
ca = float(input('Qual é o comprimento do cateto adjacente em metros?'))
hip = math.hypot(co, ca)
print(f'O comprimento da hipotenusa será de {hip}m.')