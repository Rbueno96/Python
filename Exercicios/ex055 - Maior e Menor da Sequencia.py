maior = 0
menor = 0
pessoa_maior_peso = 0
pessoa_menor_peso = 0
for pessoas in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: (kg) '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
        pessoa_maior_peso = pessoas
        pessoa_menor_peso = pessoas
    else:
        if peso > maior:
            maior = peso
            pessoa_maior_peso = pessoas
        elif peso < menor:
            menor = peso
            pessoa_menor_peso = pessoas
print('O maior peso lido foi {}Kg e pertence à {}ª pessoa.'.format(maior, pessoa_maior_peso)) #COMO COLOCAR A IDENTIFICAÇÃO
print('O menor peso lido foi {}Kg e pertence à {}ª pessoa.'.format(menor, pessoa_menor_peso)) # DA PESSOA?
