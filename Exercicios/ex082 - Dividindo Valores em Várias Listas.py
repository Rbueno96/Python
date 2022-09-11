lista = []
lista_pares = []
lista_impares = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    else:
        while continuar not in 'SN':
            continuar = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impares}')
