"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão:
-1 para binário
-2 para octal
-3 para hexadecimal. """

cores = {'verde':'\033[32m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'limpa':'\033[m'}

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para {}BINÁRIO{};
[ 2 ] converter para {}OCTAL{};
[ 3 ] converter para {}HEXADECIMAL{}'''.format(cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['amarelo'], cores['limpa']))
opçao = int(input('Sua opção é: '))
if opçao == 1:
    print('{} convertido para BINÁRIO é igual à {}{}{}'.format(num, cores['verde'], bin(num)[2:], cores['limpa']))
elif opçao == 2:
    print('{} convertido para OCTAL é igual à {}{}{}'.format(num, cores['vermelho'], oct(num)[2:], cores['limpa']))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual à {}{}{}'.format(num, cores['amarelo'], hex(num)[2:], cores['limpa']))
else:
    print('Sua opção é INVÁLIDA. Tente novamente!')

# IMPORTANTE O ''[2:]'' utilizado acima foi para remover o indicativo de transformação em binário, octal e hexadecimal