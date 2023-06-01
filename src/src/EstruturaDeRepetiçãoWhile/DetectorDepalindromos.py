print("'='*28,'Detector de palíndromos','='*28'")
frase = str(input('Digite uma frase e irei verificar se ela é um palíndromo ou não ')).lower()
fraseNova = frase.replace(' ', '').split()
inicio = len(fraseNova)
fim = len(fraseNova)
inicio = 0
fim -= 1
resultado = 1

while inicio < fim:
    if inicio == fim:
        inicio += 1    
        fim -= 1
    elif inicio != fim:
        resultado = 0
        
if resultado == 0:
    print(f'Palíndromo.')
else:
    print(f'Não é um Palíndromo.')