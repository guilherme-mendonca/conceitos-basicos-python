dis = int(input('Qual a distancia da viagem em Km? '))
if dis >= 200:
    print(f'O valor da passaagem será de R${0.45*dis:.1f}')
else:
    print(f'O valor será de R${0.50*dis:.1f}')