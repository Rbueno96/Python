import random

print('=-='*10)
print('JOGO DO PAR OU ÍMPAR')
print('=-='*10)
from random import randint
escolha_usuario = int(input('Escolha 1 ou 2, sendo que: 1 = Ímpar , 2 = Par : '))
if escolha_usuario == 1:
    print('Você escolheu Ímpar')
elif escolha_usuario == 2:
    print('Você escolheu Par')
escolha_computador = randint(0, 10)
opcao_usuario = int(input('Digite o número que quer jogar: '))
if (opcao_usuario + escolha_computador)% 2 == 0:
    resultado = 'Par'
    print('Você escolheu o número {}, e o computador escolheu o número {}. A soma deles é {}.'.format(opcao_usuario, escolha_computador, resultado))
elif (opcao_usuario + escolha_computador)% 2 == 1:
    resultado = 'Ímpar'
    print('Você escolheu o número {}, e o computador escolheu o número {}. A soma deles é {}.'.format(opcao_usuario, escolha_computador, resultado))
