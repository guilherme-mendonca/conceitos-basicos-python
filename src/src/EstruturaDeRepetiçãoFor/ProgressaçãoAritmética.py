termo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a um número para ser a razão da PA: '))
cont = termo + (10 - 1) * razao

for c in range(termo, cont+1, razao):
    print(c, end=' ')