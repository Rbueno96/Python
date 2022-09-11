"""print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
tupla = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')
preço = (1.75, 2.0, 15.9, 25, 4.2, 9.99, 120.32, 22.3, 34.9)
for item in tupla:
    print(item,'.'*50)
    for cada in preço:
        print('R${}'.format(cada), end='\n')"""

# NÃO CONSEGUI, vamos à resolução do Guanabara

# BASICAMENTE ELE FEZ COM UMA TUPLA SÓ E CONSIDERANDO QUE AS POSIÇÕES PARES SÃO OS PRODUTOS E ÍMPARES OS PREÇOS

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # MAIS UM EXEMPLO DE COMO FORMATAR COM F'
print('-'*40)
for posição in range(0, len(listagem)):  # Aqui é necessário fazer com o range para o preço ficar ao lado
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}', end='')  # Para colocar em função de f' o padrão vem dps fechando as aspas
                                        # Esse end representa que não pode quebrar a linha aqui
    else:
        print(f'R${listagem[posição]:>6.2f}')  # Aqui o .2f vem depois da informação de posicionamento

