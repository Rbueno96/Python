lista = list()
while True:
    numero = (int(input('Digire um valor: ')))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor já na lista, não vou adicionar.')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    else:
        while continuar not in 'SN':
            continuar = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f' Os numeros digitados foram {lista}')
print(f' Os numeros digitados em ordem crescente são {sorted(lista)}')
lista.sort(reverse=True)
print(f' Os numeros digitados em ordem crescente são {lista}')  #Não consegui colocar em ordem decrescente
