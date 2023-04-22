n1 = float(input(f'Digite a primeira nota: '))
n2 = float(input(f'Digite a segunda nota: '))
m = (n1+n2)/2

if m >= 7:
    print(f'Sua média é {m:.2f}. Aprovado!')

elif 5 > m > 6.9: # Se a media esta entre 5 e 6.9 recuperaçao
    print(f'Sua média é {m:.2f}. Recuperação!')

elif m < 5:
    print(f'Sua média é {m:.2f}. Reprovado!')