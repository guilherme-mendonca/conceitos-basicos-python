#014                    Conversor de temperaturas

p = bool(input('Você deseja converter celcius para fahrenheit se sim digite Y '))
c = float(input('Informe a temperatura em °C:'))
f = ((c * 9)/ 5) + 32
print(f'A temperatura de {c}°C corresponde a {f}°F')