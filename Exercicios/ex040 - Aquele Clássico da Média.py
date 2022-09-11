"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida."""

cores = {'verde':'\033[32m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'limpa':'\033[m'}
nota1 = float(input('Qual foi a primeira nota do aluno? '))
nota2 = float(input('Qual foi a segunda nota do aluno? '))
media = (nota1 + nota2)/2
if media >= 7.0:
    print('O aluno foi {}APROVADO{} com média igual à {}.'.format(cores['verde'], cores['limpa'], media))
elif media >= 5.0 and media <= 6.9:
    print('O aluno está de {}RECUPERAÇÃO{} com média igual à {}.'.format(cores['amarelo'], cores['limpa'], media))
elif media < 5.0:
    print('O aluno foi {}REPROVADO{} com média igual à {}'.format(cores['vermelho'], cores['limpa'], media))
