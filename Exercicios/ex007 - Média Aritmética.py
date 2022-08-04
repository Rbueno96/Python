print('Vamos determinar a média de um aluno e descobrir se ele foi aprovado ou reprovado.')
nome = input('Qual é o nome do aluno? ')
nota1 = float(input('Qual foi a primeira nota do {}? '.format(nome)))
nota2 = float(input('Qual foi a segunda nota do {}? '.format(nome)))
media = (nota1 + nota2)/2
if media >= 7:
    print('O aluno foi aprovado com média igual à {}'.format(media))
else:
    print("O aluno foi reprovado com média de {}".format(media))
    