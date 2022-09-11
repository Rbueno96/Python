jogadores = list()
jogador = dict()
gols = list()
cod = ''
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador["gols"] = gols.copy()
    jogador["total"] = (sum(gols))
    jogadores.append(jogador.copy())
    gols.clear()
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
    else:
        while resposta not in 'SN':
            resposta = str(input('Opção inválida. Digite apenas S ou N: ')).strip().upper()
        if resposta == 'N':
            break
print('-=-' * 15)
print(f'{"cod":<4}{"nome":<10}{"gols":<15}{"total":>10}')
print('-' * 40)
for i, a in enumerate(jogadores):
    print(f'{i:<4}{a["nome"]:<10}{a["gols"]}{a["total"]:>15}')  #NAO DA PRA FORMATAR GOLS PQ É UMA LISTA
print('-' * 40)
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break
    if cod >= len(jogadores):
        print('Não temos jogador cadastrado com esse código. Tente outro.')
    if cod <= (len(jogadores) - 1):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}:')
        k = cod
        for k, v in enumerate(jogadores[k]["gols"]):  #LEITURA: Na lista jogadores, na chave K, no valor "gols".
            print(f'No jogo {k + 1} fez {v} gols.')
    print('-' * 40)
print('----- FIM DO PROGRAMA -----')
