#026            Ocorrencias de qualquer em uma frase
frase = input('Digite uma frase: ')
letra = input('Digite uma letra: ')
frase = frase.upper()
letra = letra.upper()
print(f'A letra "{letra}" aparece {frase.count(letra)} vezes na frase.')
primeira_posicao = frase.find(letra)
ultima_posicao = frase.rfind(letra)
print(f'A letra "{letra}" aparece pela primeira vez na posição {primeira_posicao}')
print(f'A letra "{letra}" aparece pela última vez na posição {ultima_posicao}')