ano = int(input('Digite um ano qualquer e direi se ele é bissexto ou não: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0):
    print(f'O ano digitado é bissexto.')
else:
    print(f'O ano digitado não é bissexto.')