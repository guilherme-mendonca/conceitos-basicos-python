num = int(input('Digite um número inteiro: '))
cont = 0

for c in range(1, num+1): #Cria a sequência que vai do 1 até o número digitado
    if num % c == 0: #Se num for divisivel pelos números em sequência de c  o contador recebe + 1. Desse modo a variável cont guardará a quanidade de vezes que o num foi divisivel
        cont += 1

if cont == 2:
    print(f'O número {num} é primo.')
elif cont != 2:
    print(f'O número {num} não é primo.')