numero = int(input('Digite um número e veja sua tabuada: '))

print(f"\n{'='*10}Tabuada do {numero}{'='*10}\n")
for t in range(numero, numero+1):   
    for t2 in range(1, 11):
        print(f'          {t} X {t2} = {t*t2}')
print(f"\n{'='*34}")