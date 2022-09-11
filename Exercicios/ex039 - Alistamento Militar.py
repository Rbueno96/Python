"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou se passou do prazo."""

from datetime import date
nasc = int(input('Qual é o ano do seu nascimento? '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano de {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos atrás.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
