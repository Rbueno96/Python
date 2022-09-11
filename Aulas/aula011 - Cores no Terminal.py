#Código para adicionar cores ao terminal:
#\033[style,text,backm ----> Dessa forma vamos introduzir um valor para style, text e background.]

#Style: 0 = none ; 1 = bold (negrito) ; 4 = underline (sublinhado) ; 7 = negative

#Text: 30 = white ; 31 = red ; 32 = green ; 33 = yellow ; 34 = blue ; 35 = purple ; 36 = cyan ; 37 = grey ; 97 = white.

#background: o mesmo do text com 1 dezena a mais, 40, 41, 42, 43, 44, 45, 46, 47.
"""
print('\033[1;37;4mOlá, Mundo!\033[m') #A gente fecha a mensagem com a flag m.
nome = str(input('Qual é o seu nome e sobrenome? ')).strip()
separado = nome.split()
print(separado)
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m')) #serão 3 {}, uma para cada

"""

nome = 'Rodrigo Bueno'.split()
cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[0;33m',
         'pretoebranco':'\033[7;30m'}

print('{}Olá, Mundo!'.format(cores['azul']))
print('Olá, {}{}{} {}{}{}! Muito prazer em conhecê-lo!'.format(cores['amarelo'], nome[0], cores['limpa'], cores['azul'], nome[1], cores['limpa']))
