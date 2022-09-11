# NESSA OUTRA RESOLUÇÃO PODEMOS CRIAR UMA LISTA DE OPÇÕES
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input("""ESCOLHA DENTRE AS OPÇÕES ABAIXO A JOGADA CORRESPONDENTE:
[ 0 ] -> PEDRA
[ 1 ] -> PAPEL
[ 2 ] -> TESOURA
QUAL É A SUA JOGADA? """))
print('=-='*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('=-='*20)
print('Você escolheu {} e o computador escolheu {}'.format(itens[jogador], itens[computador]))
if jogador == 0:
    if computador == 0:
        print('EMPATE!')
    elif computador == 1:
        print('VOCÊ PERDEU!')
    elif computador == 2:
        print('VOCÊ VENCEU!')
elif jogador == 1:
    if computador == 0:
        print('VOCÊ VENCEU!')
    elif computador == 1:
        print('EMPATE!')
    elif computador == 2:
        print('VOCÊ PERDEU!')
elif jogador == 2:
    if computador == 0:
        print('VOCÊ PERDEU!')
    elif computador == 1:
        print('VOCÊ VENCEU!')
    elif computador == 2:
        print('EMPATE!')
else:
    print('OPÇÃO INVÁLIDA, ANIMAL!')
