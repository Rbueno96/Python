nome = str(input('Qual é o seu nome completo? ')).strip()
separado = nome.split()
print(separado)
print('O seu primeiro nome é {}'.format(separado[0]))
print('O seu último nome é {}'.format(separado[len(separado)-1]))
