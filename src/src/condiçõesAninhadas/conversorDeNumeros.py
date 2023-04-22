num = int(input('Digite um número inteiro: ')) #Colocando 3 aspas podemos 
print('''Escolha uma das bases para conversão
1-Converter para Binário
3-Converter para Hexadecimal
2-Converter para Octal''')
op = int(input('Opção: '))

if op == 1: 
    print(f'O número {num} convertido para Binário é igual a {bin(num)}.')
elif op == 2:
    print(f'O número {num} convertido para Hexadecimal é igual a {hex(num)}.')
elif op == 3:
    print(f'O número convertidp para Octal é igual a {oct(num)}.')
else:
    print('Opção inválida por faavor tente novamente.')