nome = str(input('Qual é o seu nome? '))
if nome == 'Guilherme':
    print('Que nome bonito!')
    
#elif é sempre depois de if     
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
    
elif nome in 'Júlia Fernanda Ana Rayssa': #procura se tem a variavel nome é igual a um do nomes escritos
    print('Belo nome feminino.')

else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')