#t = int(input('Digite o tempo:'))
#d = int(input('Digite a distância:'))
#v = float(print('A velocidade média é {}'.format(d/t)))

#n1 = int(input('Digite um valor:'))
#n2 = int(input('Digite outro valor:'))
#s = n1 + n2
#su = n1 - n2
#m = n1 * n2
#d = n1 / n2
#di = n1 // n2
#e = n1 ** n2
#para quebrar a linha use \n ; para nao quebrar a linha no final do codigo utilize end=' '
#print(f'A soma é {s}; a subtração é {su}; o produto é {m}; a divisão é {d:.3f}; a divisão inteira é {di} e a potência é {e}.',)

#n = int(input('Digite um número para saber seu antecessor e seu sucessor '))
#a = n-1
#s = n+1
#print(f'O número digitado foi {n}, seu antecessor é {a} e o seu sucessor é {s}')

#                                           Dobro, triplo e raiz
#n = float(input('Digite um valor: '))
#d = n * 2
#t = n * 3
#r = n **(1/2)
#print(f'O número digitado foi {n}, o seu dobro é {d}, e o seu triplo é {t} e a sua raiz quadrada é {r:.3f}')

#008                                         Conversor de metros
#m = float(input('Quantos metros? '))
#c = (m*100)
#mi = (c*10)
#print(f'{m} metros. Convertendo em centímetros temos {c:.0f}cm. Convertendo em milímetros temos {mi:.0f}mm')

#009                                           tabuada
#n = int(input('Digite um número para saber sua tabuada! '))
#t1 = (n*1)
#t2 = (n*2)
#t3 = (n*3)
#t4 = (n*4)
#t5 = (n*5)
#t6 = (n*6)
#t7 = (n*7)
#t8 = (n*8)
#t9 = (n*9)
#t10 = (n*10)
#print(f'Veja a tabuada de {n} a seguir ') 
#print('='*120)
#print(f'{n:>40} X 1 = {t1:<40}')
#print(f'{n:>40} X 2 = {t2:<40}')
#print(f'{n:>40} X 3 = {t3:<40}')
#print(f'{n:>40} X 4 = {t4:<40}')
#print(f'{n:>40} X 5 = {t5:<40}')
#print(f'{n:>40} X 6 = {t6:<40}')
#print(f'{n:>40} X 7 = {t7:<40}')
#print(f'{n:>40} X 8 = {t8:<40}')
#print(f'{n:>40} X 9 = {t9:<40}')
#print(f'{n:>40} X 10 = {t10:<40}')
#print('='*120)

#010                               Conversor de reais para dolar
#r = float(input('Digite quantos um valor em reais: '))
#d = (r/3.27)
#print(f'Você tem R${r:.2f} real. Convertendo é possível comprar USS{d:.2f} dólares!')

#011                               Litros de tinta por area da parede
#l = float(input('Qual é a largura da parede em metros à ser pintada?'))
#h = float(input('Qual é a altura da parede metros à ser pintada?'))
#a = (l*h)
#lt = (a/2)
#print(f'Sua parede tem a dimensão de {l} X {h} e sua área é de {a}m². \n Para pintar essa parede, você  precisará de {lt}l de tinta.')

#012                      Desconto (porcentagem)
#v = float(input('Qual é o preço da mercadoria?'))
#d = float(input('Quanto é o desconto?'))
#vd = v - (v * d / 100)
#print(f'O produto custa {v:.2f}, com o desconto de {d:.2f}% o produto irá custar R${vd:.2f} reais.')

#013                      Aumento de salario (porcentagem)

#s = float(input('Quanto é o salário?'))
#a = float(input('Quanto é o valor de aumento?'))
#sn = (((a*s)/100)+s)
#print(f'Antes o seu salário era de {s:.2f}, com {a:.0f}% de aumento você passa a receber R${sn:.2f}')

#007                     Media aritmetica
#nota1 = float(input('Primeira nota do aluno:'))
#nota2 = float(input('Segunda nota do aluno:'))
#media = ((nota1+nota2)/2)
#print(f'A média entre {nota1:.1f} e {nota2:.1f} é igual a {media:.1f}')

#014                    Conversor de temperaturas

#p = bool(input('Você deseja converter celcius para fahrenheit se sim digite Y '))

#c = float(input('Informe a temperatura em °C:'))
#f = ((c * 9)/ 5) + 32
#print(f'A temperatura de {c}°C corresponde a {f}°F') 

#015                      Aluguel de carros
#da = int(input('Quantos dias alugados?'))
#kr = float(input('Quantos km rodados?'))
#t = (da * 60)+(kr * 0.15)
#print(f'O total a pagar é de R${t:.2f}')

#from math import sqrt, floor           #quando importamos toda a biblioteca precisamos cita-la antes da #função difrente se inportamos uma função especifica como visto no codigo
#num = int(input('Digite um número:'))
#raiz = sqrt(num)
#print(f'A raiz de {num} é {floor(raiz)}')

#import random       #randint voce gera um numero inteiro
#num = random.randint(1, 7)
#print(num)

#016                    A porção inteira
#from math import floor
#num = float(input('Digite um número decimal: '))
#print(f'O número decimal {num} tem a parte inteira {floor(num)}.')

#017                    Pitágoras
#import math
#co = float(input('Qual é o comprimento do cateto oposto em metros?'))
#ca = float(input('Qual é o comprimento do cateto adjacente em metros?'))
#hip = math.hypot(co, ca)
#print(f'O comprimento da hipotenusa será de {hip}m.')

#018                        Angulo sen, cos e tan

#import math
#an = float(input('Qual é o ângulo desejado? '))
#sen = math.sin(math.radians(an))
#cos = math.cos(math.radians(an))
#tan = math.tan(math.radians(an))
#print(f'O valor do seno será {sen:.2f}, o valor de cos {cos:.2f} e o da tangente {tan:.2f}.')

#019                        Sorteio dos nomes

#import random
#nome1 = str(input('Digite o nome do primeiro a ser sorteado: '))
#nome2 = str(input('Dgite o nome do segundo a ser sorteado: '))
#nome3 = str(input('Digite o nome do terceiro a ser sorteado: '))
#nome4 = str(input('Digite o nome do quarto a ser sorteado: '))
#nomes = [nome1, nome2, nome3, nome4]
#print(f'A pessoa sorteada foi.......{random.choice(nomes)}!')

#020                      Sorteio da ordem de apresetação 

#import random
#nom1 = str(input('Digite o nome do preimeiro aluno: '))
#nom2 = str(input('Dgite o nome do segundo aluno: '))
#nom3 = str(input('Digite o nome do terceiro aluno: '))
#nom4 = str(input('Digite o nome d oquarto aluno: '))
#sorteado = [nom1, nom2, nom3, nom4]
#random.shuffle(sorteado)
#print(f'A ordem de apresentação será {sorteado}')

#021                    Reprodução de audio

#from playsound import playsound
#playsound(r'C:\Users\gabri\Documents\guilherme\Guilherme-programação\python/beat.mp3')

#           Fatiamento de strings
#frase = 'A cobra Vai fumar'
#print(frase[::5])   #vai recortar a frase do começo ate o final de 5 em 5
#print[1:12:1]  #vai recortar a frase do 1 ao 12 pulando de dois em dois
#print(frase.upper().count('A'))
#print(len(frase.strip()))
#print(frase.replace('fumar', 'dançar'))   #vai trocar a palavra fumar para dançar
#print('cobra' in frase)   #vai dizer se existe a palavra ou letra na frase
#print(frase.lower().find('Vai'))      #vai procurar se existe a palavra mencionada se ela nao existir retona -1, se existir ela fala a enumeração de odne comeca a palavra

#frase2 = 'Curso em Vídeo Python'
#dividido = frase2.split()
#print(dividido[2] [3])

#022                    O seu nome               
frase = input('Digite seu nome completo: ')
print(f'O seu nome com todas as letras MAIÚSCULAS: {(frase.upper())}')  #todas as letras em maiúculas
print(f'O seu nome com todas as letras minúsculas: {(frase.lower())}')  #todas as letras em minúsculas
espacovazio = frase.count(' ')  #vai contar os espaços no seu nome
espacotodo = len(frase)  #vai ler o o nome contando com os espaços
print(f'O seu nome possui {(espacotodo - espacovazio)} letras.')   #O espaço total menos o espaço vazio que é igual ao numero de letras
di = frase.split()  #dividi a string em partes    
print(f'O núemro de letras do seu primeiro nome é: {(len(di[0]))}')   #Print do numero de letras de uma das pertes divididas

#023                Unidade dos números
#num = str(input('Digite um número de 0 a 9999: '))
#di = num.split()
#print(f'Unidade: {(di[0] [3])}')
#print(f'Dezena: {(di[0] [2])}')
#print(f'Centena: {(di[0] [1])}')
#print(f'Milhar: {(di[0] [0])}')

#024                        Santo no nome da cidade
#city = str(input('Digite o nome de uma cidade: '))
#di = city.upper().split()
#print(f"True se a cidade ter 'santo' no começo do nome e False se ela não tiver. \n {'SANTO' in di[0]}")

#025                        Sila no nome
#nome = input('Digite seu nome completo: ')
#nome = nome.upper()
#print(f'True se o seu nome ter "SILVA" e False se não tiver. \n {"SILVA" in nome}')

#026                        leitura de um frase
