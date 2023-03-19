#       Praticas de aprendizado comentadas

t = float(input('Digite o tempo em horas:'))
d = float(input('Digite a distância:'))
(print('A velocidade média é {:.2f}Km/h'.format(d/t)))

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# para quebrar a linha use \n ; para nao quebrar a linha no final do codigo utilize end=' '
print(f'A soma é {s}; a subtração é {su}; o produto é {m}; a divisão é {d:.3f}; a divisão inteira é {di} e a potência é {e}.',)

n = int(input('Digite um número para saber seu antecessor e seu sucessor '))
a = n-1
s = n+1
print(f'O número digitado foi {n}, seu antecessor é {a} e o seu sucessor é {s}')


import random       #randint voce gera um numero inteiro
num = random.randint(1, 7)
print(num)
do = n * 2
tr = n*3
r = n **(1/2)
print(f'O número digitado foi {n}, o seu dobro é {do}, e o seu triplo é {tr} e a sua raiz quadrada é {r:.3f}')

#           Fatiamento de strings
frase = 'Python é muito divertido'
print(frase[::5])   #vai recortar a frase do começo ate o final de 5 em 5
print[1:3:1]  #vai recortar a frase do 1 ao 12 pulando de dois em dois
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Dançar'))   #vai trocar a palavra fumar para dançar
print('muito' in frase)   #vai dizer se existe a palavra ou letra na frase
print(frase.lower().find('é'))      #vai procurar se existe a palavra mencionada se ela nao existir retona -1, se existir ela fala a enumeração de odne comeca a palavra

frase2 = 'Curso em Vídeo Python'
dividido = frase2.split()
print(dividido[2] [3])