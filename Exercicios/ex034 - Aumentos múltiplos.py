salario = float(input('Digite o salário do funcionário: R$ '))
if salario >= 1250.0:
    aumento = salario * 1.1
    print('O valor corrigido, com o aumento de 10%, será de R${:.2f}.'.format(aumento))
elif salario < 1250.0:
    aumento = salario * 1.15
    print('O valor corrigido, com o aumento de 15%, será de R${:.2f}.'.format(aumento))
