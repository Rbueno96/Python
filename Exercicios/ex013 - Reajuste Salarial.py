salario = float(input('Digite o salário do funcionário: R$'))
aumento = float(input('Digite o aumento que o funcionário receberá em %: '))
valor = (salario * (1 + (aumento/100)))
print('O funcionário que antes ganhava {:.2f}, e teve aumento de {:.1f}%, passará à receber R${:.2f}.'.format(salario, aumento, valor))
