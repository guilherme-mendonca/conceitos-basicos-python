n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1     #Considerando o n1 como menor não precisamos fazer outra condição
#Verificando quem é menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificand quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n2:
    maior = n3
print(f'O maior número é {maior} ')
print(f'O menor número é {menor} ')