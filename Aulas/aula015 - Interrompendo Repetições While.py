# CONDIÇÕES PARA CRIAR UM WHILE INFINITO E INTERROMPER ESSE WHILE
# PARA CRIAR O WHILE INFINITO UTILIZAMOS O '' WHILE TRUE ''
# PARA INTERROMPER UTILIZAMOS O COMANDO '' BREAK ''

"""numero = soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        soma += numero
print('A soma é igual à {}'.format(soma))"""

"""numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print('A soma é igual à {}'.format(soma))"""

# Nova forma de usar uma função '' f '' de uma string e variável:

nome = 'José'
idade = 33
salario = 983.4
print(f'O {nome:-^20} tem {idade} anos e ganha atualmente R${salario:.2f}')
# A formatação das casas variáveis vem depois da variável.

