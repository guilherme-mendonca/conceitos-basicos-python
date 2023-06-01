s = 0 #O acumulador 
cont = 0 

for c in range(1, 501, 2):
    if c % 3 == 0: # Se o resto da divisão por 3 for exata ou seja se for divisivel por 3
        cont += 1  #   um cont normalmente soma 1, conta mais 1
        s += c # s = s + c   um acumulador normalmente soma  UM VALOR
print(f'A soma de todos os {cont} valores solicitados é {s}.')