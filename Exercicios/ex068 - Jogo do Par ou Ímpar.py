from random import randint
print('{:-^60}'.format(' PAR OU ÍMPAR '))
usuario = computador = 0
nome = str(input('Qual é o seu nome? '))
print(f'Olá {nome}, como você está? Preparada para esse jogo? Então, vamos.')
while True:
    valor_computador = randint(0, 10)
    valor_usuario = int(input('Diga um valor: '))
    escolha_usuario = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0] # 0 para pegar a primeira string
    # escolha_usuario = '' ; while escolha_usuario not in 'PpIi':  Outra forma de garantir que o usuário insira correto
    if escolha_usuario == 'P':
        escolha_usuario = 'PAR'
    elif escolha_usuario == 'I':
        escolha_usuario = 'ÍMPAR'
    soma = valor_usuario + valor_computador
    if soma % 2 == 0:
        resultado = 'PAR'
    elif soma % 2 != 0:
        resultado = 'ÍMPAR'
    print(f'O usuário escolheu {valor_usuario}, o computador escolheu {valor_computador}.')
    print(f'A soma dos valores é igual à {soma} que é {resultado}.')
    if escolha_usuario == resultado:
        print('Você GANHOU!')
        print('-' * 20)
        usuario += 1
    elif escolha_usuario != resultado:
        print('Você PERDEU!')
        print('-'*20)
       # print(f'GAME OVER! Você venceu {usuario} vezes.')
       # break
        computador += 1
    print(f'PLACAR: {nome} {usuario} x {computador} Computador')
