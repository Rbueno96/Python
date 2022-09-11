galera = []
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    else:
        while continuar not in 'S/N':
            continuar = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maior}Kg', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'e pertence à {p[0]}')
print()
print(f'O menor peso foi de {menor}Kg', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'e pertence à {p[0]}')
print()
