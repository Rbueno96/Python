from time import sleep
from random import randint
import sys  #MÓDULO DE SISTEMA
print('{:=^36}'.format(' JO KEN PO '))
escolha_jogador = int(input("""Escolha a opção correspondente à sua jogada:
[ 0 ] -> PEDRA
[ 1 ] -> PAPEL
[ 2 ] -> TESOURA
QUAL É A SUA JOGADA? """))
if escolha_jogador == 0:
    escolha_jogador = 'PEDRA'
    print('Você escolheu PEDRA!')
elif escolha_jogador == 1:
    escolha_jogador = 'PAPEL'
    print('Você escolheu PAPEL!')
elif escolha_jogador == 2:
    escolha_jogador = 'TESOURA'
    print('Você escolheu TESOURA!')
else:
    print('Você não escolheu uma opção válida!')
    sys.exit() #INTERROMPE A EXECUÇÃO.
escolha_computador = randint(0, 2)
if escolha_computador == 0:
    escolha_computador = 'PEDRA'
elif escolha_computador == 1:
    escolha_computador = 'PAPEL'
elif escolha_computador == 2:
    escolha_computador = 'TESOURA'
print('=-='*30)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('=-='*30)
print('Você escolheu {} e o computador escolheu {}.'.format(escolha_jogador, escolha_computador))
if escolha_jogador == escolha_computador:
    print('EMPATE!')
elif escolha_jogador == 'PEDRA' and escolha_computador == 'TESOURA':
    print('Você VENCEU!')
elif escolha_jogador == 'PEDRA' and escolha_computador == 'PAPEL':
    print('Você PERDEU!')
elif escolha_jogador == 'PAPEL' and escolha_computador == 'PEDRA':
    print('Você VENCEU!')
elif escolha_jogador == 'PAPEL' and escolha_computador == 'TESOURA':
    print('Você PERDEU!')
elif escolha_jogador == 'TESOURA' and escolha_computador == 'PAPEL':
    print('Você VENCEU!')
elif escolha_jogador == 'TESOURA' and escolha_computador == 'PEDRA':
    print('Você PERDEU!')
