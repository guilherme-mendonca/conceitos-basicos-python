#012                      Desconto (porcentagem)
v = float(input('Qual é o preço da mercadoria? '))
d = float(input('Quanto é o desconto? '))
vd = v - (v * d / 100)
print(f'O produto custa {v:.2f}, com o desconto de {d}% o produto irá custar R${vd:.2f} reais.')