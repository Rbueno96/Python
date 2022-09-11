from datetime import date
dados = {}
dados['nome'] = str(input('Nome: ')).strip().capitalize()
dados['nascimento'] = int(input('Ano de Nascimento: '))
idade = date.today().year - dados['nascimento']
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
print('-=' * 30)
for k, v in dados.items():
    if k == 'nome':
        print('-', f'Seu {k} é {v}')
    elif k == 'nascimento':
        print('-', f'Seu {k} foi em {v} e você tem {idade} anos')
    elif k == 'ctps':
        print('-', f'Sua {k} possui o número de registro {v}')
    elif k == 'contratação':
        print('-', f'Sua {k} ocorreu no ano de {v}')
    elif k == 'salário':
        print('-', f'Seu {k} tem o valor de R${v:.2f}.')
print('FIM DO PROGRAMA')