#011                               Litros de tinta por area da parede
l = float(input('Qual é a largura da parede em metros à ser pintada?'))
h = float(input('Qual é a altura da parede metros à ser pintada?'))
a = (l*h)
lt = (a/2)
print(f'Sua parede tem a dimensão de {l} X {h} e sua área é de {a}m². \n Para pintar essa parede, você  precisará de {lt}l de tinta.')