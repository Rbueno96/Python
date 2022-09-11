lista = []
while True:
    numero = (int(input('Digite um valor: ')))
    lista.append(numero)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()
lista.sort(reverse=True)  # Não dá pra utilizar o reverse dentro do print formatado
print(f'Você digitou a lista de número em ordem decrescente {lista}')
print(f'Você digitou {len(lista)} elementos.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
