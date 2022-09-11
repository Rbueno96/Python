"""A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de
um atleta e mostre sua categoria, de acordo com a idade:"""

from datetime import date
nome = str(input('Qual é o nome do atleta? '))
nasc = int(input('Qual é o ano do seu nascimento? '))
idade = date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL.')
elif 14 < idade <= 19:
    print('Sua categoria é JUNIOR.')
elif 19 < idade <= 25:
    print('Sua categoria é SÊNIOR.')
elif idade > 25:
    print('Sua categoria é MASTER.')
