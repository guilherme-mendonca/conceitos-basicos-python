#020                      Sorteio da ordem de apresetação 
import random
nom1 = str(input('Digite o nome do preimeiro aluno: '))
nom2 = str(input('Dgite o nome do segundo aluno: '))
nom3 = str(input('Digite o nome do terceiro aluno: '))
nom4 = str(input('Digite o nome d oquarto aluno: '))
sorteado = [nom1, nom2, nom3, nom4]
random.shuffle(sorteado)
print(f'A ordem de apresentação será {sorteado}')