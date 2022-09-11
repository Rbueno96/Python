print('-'*50)
print('{:^50}'.format('LOJAS SUPER BARATÃO'))
print('-'*50)
contagem = 0
total = 0
produto_acima = 0
menor_valor = 0
produto_menor = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().title()
    preço = float(input('Preço: R$'))
    if contagem == 0:
        menor_valor = preço
        contagem += 1
    if preço > 1000:
        produto_acima += 1
    if preço <= menor_valor:
        menor_valor = preço
        produto_menor = produto
    total += preço
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^50}'.format(' FIM DO PROGRAMA ')) # É dois pontos tal coisa centralizado em 50 espaços
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {produto_acima} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {produto_menor} que custa R${menor_valor:.2f}.')
