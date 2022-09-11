"""lista = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')).strip().capitalize())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    lista.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    else:
        while continuar not in 'SN':
            continuar = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()
print('-=-' * 30)
print(f'{"No.":<5}', f'{"NOME":<20}', f'{"MÉDIA":<5}')
print('-' * 30)


while not 999:

print(lista)"""

ficha = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opçao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opçao == 999:
        print('FINALIZANDO...')
        break
    if opçao <= len(ficha) - 1:
        print(f'Notas de {ficha[opçao][0]} são {ficha[opçao][1]}')
print('<<< VOLTE SEMPRE >>>')
