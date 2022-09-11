media = 0
homem_maior_idade = 0
nome_homem_maior_idade = 0
mulheres = 0
mulheres_menor_idade = 0
for pessoas in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoas))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    media += idade
    if pessoas == 1 and sexo in 'Mm':
        homem_maior_idade = idade
        nome_homem_maior_idade = nome
    elif pessoas == 1 and sexo in 'Ff':
        mulheres += 1
        if idade < 20:
            mulheres_menor_idade += 1
    else:
        if idade > homem_maior_idade and sexo in 'Mm':
            homem_maior_idade = idade
            nome_homem_maior_idade = nome
        elif sexo in 'Ff':
            mulheres += 1
            if idade < 20:
                mulheres_menor_idade += 1
print('A média de idade do grupo é de {} anos.'.format(media/pessoas))
print('O homem mais velho tem {} anos e se chama {}.'.format(homem_maior_idade, nome_homem_maior_idade))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres_menor_idade))
