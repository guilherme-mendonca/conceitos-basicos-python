#015                      Aluguel de carros
da = int(input('Quantos dias alugados?'))
kr = float(input('Quantos km rodados?'))
t = (da * 60)+(kr * 0.15)
print(f'O total a pagar é de R${t:.2f}')