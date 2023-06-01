#022                    Quantas letras tem o seu preimeiro nome e ele todo            
frase = input('Digite seu nome completo: ')
print(f'O seu nome com todas as letras MAIÚSCULAS: {(frase.upper())}')  #todas as letras em maiúculas
print(f'O seu nome com todas as letras minúsculas: {(frase.lower())}')  #todas as letras em minúsculas
espacovazio = frase.count(' ')  #vai contar os espaços no seu nome
espacotodo = len(frase)  #vai ler o nome contando com os espaços
print(f'O seu nome possui {(espacotodo - espacovazio)} letras.')   #O espaço total menos o espaço vazio que é igual ao numero de letras
di = frase.split()  #dividi a string em partes    
print(f'O núemro de letras do seu primeiro nome é: {(len(di[0]))}')   #Print do numero de letras de uma das pertes divididas