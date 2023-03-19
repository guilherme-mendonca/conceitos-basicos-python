vel = int(input('Qual a velocidade do carro em Km/h? '))
print("="*7,'O limite da via é 80Km/h.',"="*7)
if vel >= 80:
    print(f'Sua velocidade é de {vel}Km/h, você excedeu o limite de velocidade da via!')
    val = (vel - 80)
    mul = (val * 7)
    print(f'Sua multa será de {mul} reais.')
else:
    print(f'Sua velocidade é de {vel}Km/h. Não ultrapasse o limite da via.')
print('Dirija com segurança, use o cinto.')