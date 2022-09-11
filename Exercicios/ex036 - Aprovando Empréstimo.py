"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
negado."""

cores = {'green':'\033[32m',
         'red':'\033[31m',
         'limpa':'\033[m'}
nome = str(input('Saudações, qual é o seu nome? '))
valor_casa = float(input('Qual é o valor da casa em reais? R$'))
salario = float(input('Qual é o salário do comprador em reais? R$'))
tempo_anos = int(input('Em quantos anos você vai pagar? '))
tempo_meses = 12 * tempo_anos
prestaçao = (valor_casa/tempo_meses)
if prestaçao <= (0.3 * salario):
    print('O empréstimo foi AUTORIZADO. O valor da prestação é de R${}{:.2f}{}'.format(cores['green'], prestaçao, cores['limpa']))
else:
    print('O empréstimo foi NEGADO. Pois o valor da prestação é de R${}{:.2f}{} e ultrapassa o limite de 30% de R${:.2f}'.format(cores['red'], prestaçao, cores['limpa'], salario))
