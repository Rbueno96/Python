"""from random import randint
print('Sou seu computador...')
num_computador = randint(0, 10)
num_usuario = ''
tentativas = 0
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
while num_computador != num_usuario:
    num_usuario = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if num_usuario == num_computador:
        print('PARABÉNS, você acertou depois de {} tentativas!'.format(tentativas))
    elif num_usuario > num_computador:
        print('MENOS... Tente mais uma vez: ')
    elif num_usuario < num_computador:
        print('MAIS... Tente mais uma vez: ')"""

# RESOLUÇÃO DO GUANABARA

from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} palpites.' .format(palpites))
