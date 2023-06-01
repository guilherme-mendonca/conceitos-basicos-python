print('='*28,'Detector de palíndromos','='*28)
frase = str(input('Digite uma frase e irei verificar se ela é um palíndromo ou não. \n')).lower().strip() #O .strip() tira os espaços externos da frase.
fraseNova = frase.replace(' ', '') #No lugar de replace poderia ser colocado  o ''.join(frase) que irá subtistuir os espaços da palavra por algum caractere ou nenhum.
inicio = 0 #inicio recebe 0, pois ele gurdara o numero da primeira letra da frase 
fim = len(fraseNova) -1 #Define a variavel fim como o comprimento da faseNnova -1 tanto o inicio como o fim serão usadas para percorrer a frase dos extremos.
resultado = 1 #Essa variáve será usada para indicar se um frase for palíndromo(1) ou não(2).
                                #Para chegar ao número de letras da palavra é o total de letra menos 1 letra a ultima letra menos 1; O -1 depois é a primeira letra(0) e o -1; E o outro -1 é para voltar pois a frase deve ficar invertida.
for c in range(len(fraseNova)): #Outro metodo seria (len(fraseNova) - 1, - 1, -1)
    if fraseNova[inicio] != fraseNova[fim]: #verifica se os caracteres nas posições 'inicio' e 'fim' são diferenres. Se sim, o 'resultado' vai ser igual a 0 e sai do loop com o break.
        resultado = 0
        break #Se a condição for verdadeira sai do loop
    inicio += 1 #incrementa o 'inicio' para avançar na verificação dos caracteres da frase.
    fim -= 1    #decrementa o 'fim'.

if resultado == 1:
    print(f'Palíndromo.')
else:
    print(f'Não é um Palíndromo.')