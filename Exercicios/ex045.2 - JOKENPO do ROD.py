from time import sleep
from random import randint
cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'amarelo':'\033[0;33m',
         'vermelho':'\033[0;31m',
         'verde':'\033[0;32m'}
nome = str(input('Saudações humano. Vamos jogar um jogo. Qual é o seu nome? ')).capitalize().strip()
lista_opçoes = ['PEDRA', 'PAPEL', 'TESOURA']
placar_usuario = placar_computador = contador = 0
while True:
    print('=--=' * 30)
    print("""Vamos jogar JOKENPO! O PRIMEIRO A MARCAR 5 PONTOS GANHA.
     Escolha a opção correspondente à sua jogada:
[ 0 ] -> PEDRA
[ 1 ] -> PAPEL
[ 2 ] -> TESOURA""")
    escolha_usuario = int(input('Qual é a sua jogada? '))
    sleep(1)
    print('Estou pensando na minha jogada...')
    sleep(1)
    escolha_computador = randint(0, 2)
    if escolha_usuario == 0:
        if escolha_computador == 0:
            print('\033[33m''EMPATE!''\033[m')
        elif escolha_computador == 1:
            print('VOCÊ''\033[31m' ' PERDEU''\033[m'' essa rodada.')
            placar_computador += 1
        elif escolha_computador == 2:
            print('VOCÊ''\033[32m' ' VENCEU''\033[m'' essa rodada.')
            placar_usuario += 1
    if escolha_usuario == 1:
        if escolha_computador == 1:
            print('\033[33m''EMPATE!''\033[m')
        elif escolha_computador == 2:
            print('VOCÊ''\033[31m' ' PERDEU''\033[m'' essa rodada.')
            placar_computador += 1
        elif escolha_computador == 0:
            print('VOCÊ''\033[32m' ' VENCEU''\033[m'' essa rodada.')
            placar_usuario += 1
    if escolha_usuario == 2:
        if escolha_computador == 2:
            print('\033[33m''EMPATE!''\033[m')
        elif escolha_computador == 0:
            print('VOCÊ''\033[31m' ' PERDEU''\033[m'' essa rodada.')
            placar_computador += 1
        elif escolha_computador == 1:
            print('VOCÊ''\033[32m' ' VENCEU''\033[m'' essa rodada.')
            placar_usuario += 1
    print('\033[34m''PLACAR: ''\033[m''\033[35m'f'{nome.upper()} {placar_usuario}''\033[m'' X ' '\033[33m' f'{placar_computador}'
          ' COMPUTADOR''\033[m')
    if placar_usuario == 5:
        print(f'Parabéns! {cores["verde"]} Você VENCEU!'f'{cores["limpa"]}')
        break
    elif placar_computador == 5:
        print(f'Que pena! {cores["vermelho"]} Você PERDEU!'f'{cores["limpa"]}')
        break
print(f'Obrigado por jogar comigo {nome}. Volte sempre! :)')