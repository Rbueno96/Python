# aluno = {'nome': str(input('Nome: '))}   Uma outra opção é criar direto a primeira chave
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('==' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual à {v}')
