feminino_menor_idade = 0
masculino = 0
menor_idade = 0
maior_idade = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade > 18:
        maior_idade += 1
    elif idade < 18:
        menor_idade += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F' and idade < 18:
        feminino_menor_idade += 1
    else:
        while sexo not in "MF":
            print('Opção inválida. Escolha uma das opções:')
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
            if sexo == 'M':
                masculino += 1
            elif sexo == 'F' and idade < 18:
                feminino_menor_idade += 1
    print('-' * 20)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
    else:
        print('Opção inválida. Escolha uma das opções:')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'Total de pessoas com mais de 18 anos: {maior_idade}.')
print(f'Ao todo temos {masculino} homens cadastrados.')
print(f'E temos {feminino_menor_idade} mulheres com menos de 20 anos.')
print('Fim do cadastramento.')

"""Resolução do Guanabara, código mais limpo
    No caso ele fez um while True para sexo e outro while True para a resposta.

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18: 
        tot18 += 1 
        
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N'
        break
        
        """


