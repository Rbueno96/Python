nome = str(input('Qual é o seu nome? ')).strip()
silva = (nome.upper().find('SILVA'))
if silva == -1:
    print('Você não possui Silva no nome')
else:
    print('Você possui Silva no nome')

#outra forma

"""nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
"""