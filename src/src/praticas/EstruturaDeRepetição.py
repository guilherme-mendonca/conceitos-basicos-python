#laço c no intervalo(1,10)       for c in range(1,10):
#    passo                           passo                    
#pega                            pega                        

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p): #No python s = s + n => s += n 
    print(c)
print('fim!')    


n = int(input('Digite um número: ')) 
for c in range(1, n+1):
    print(c)
print('FIM!!!')

for c in range(0,4): #O último número não é considerado entao para contar ate 3 colocamos o proximo numero.  
    print(c)
print('Fim!\n')

for c in range(5, 0, -1):#Para contar em ordem decrescente colocamos -1 no final e colocamos o ultimo número em primeiro e o primeiro em segundo
    print(c)
print('fim\n')

for c in range(0, 9, 2): #Para contar apenas os número pares adicionamos o numero 2 no final
    print(c)
print('Fim')

for c in range(1, 10, 2): #Para contar apenas os número inpares colocamos o 1 no lugar do 0
    print(c)
print('Fim!!')

#Programa que coloca qualquer frase invertida

frase = str(input('Digite um frase para vê-la de trás para frente: \n'))
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) -1 , -1, -1):
    inverso += len(junto[letra])
print(f'Sua frase de trás para frente é {inverso}')