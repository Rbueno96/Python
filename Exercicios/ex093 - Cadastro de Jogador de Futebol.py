jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
print('-=-' * 20)
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(jogador)
print('-=-' * 20)
for k, v in jogador.items():
    if k == 'nome':
        print('-', f'O {k} do jogador é {v};')
    elif k == 'gols':
        print('-', f'Ele marcou {v} {k};')
    elif k == 'total':
        print('-', f'O {k} de gols nessas partidas foi {v}.')
print('-=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print('->', f'Na partida {k+1}, fez {v} gols;')
print(f'Foi um total de {sum(gols)} gols.')