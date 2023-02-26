#019                        Sorteio dos nomes

import random
nome1 = str(input('Digite o nome do primeiro a ser sorteado: '))
nome2 = str(input('Dgite o nome do segundo a ser sorteado: '))
nome3 = str(input('Digite o nome do terceiro a ser sorteado: '))
nome4 = str(input('Digite o nome do quarto a ser sorteado: '))
nomes = [nome1, nome2, nome3, nome4]
print(f'A pessoa sorteada foi.......{random.choice(nomes)}!')
