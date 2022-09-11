dados = {}
pessoas = []
soma = media = 0
mulheres = []
while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    dados['sexo'] = str(input('Sexo [M/F]:  ')).strip().upper()
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Opção inválida. Digite a opção correspondente. Sexo [M/F]:  ')).strip().upper()
    if dados['sexo'] == 'F':
        mulheres.append(dados["nome"])
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'S':
        continue
    if resp == 'N':
        break
    else:
        while resp not in 'SN':
            resp = str(input('Opção inválida. Digite a opção para continuar ou parar. Continuar? [S/N] '
                             )).strip().upper()
        if resp == 'N':
            break
for k, v in enumerate(pessoas):
    soma += pessoas[k]["idade"]  #Como é uma lista, o primeiro é o KEY e dps o dicionário, não é um número.
media = (soma / (len(pessoas)))
print('-=-' * 20)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media}')
print(f'C) As mulheres cadastradas são {", ".join(mulheres)}')  #Join retira os [] e as ''
print(f'D) Lista das pessoas que estão acima da média de idade:')
for p in pessoas:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<<< FIM DO PROGRAMA >>>')
