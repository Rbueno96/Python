def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não mostrar a situação do aluno
    :return: dicionário com várias informações sobre a situação da turma.
    """
    aluno = dict()
    aluno['nome'] = str(input('Aluno: '))
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n)/len(n)
    if sit:
        if aluno['media'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['media'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


# Programa Principal:
resp = notas(5.5, 2.5, 8.5, sit=True)  #Dessa forma eu passo mais um parâmetro para ele retornar, if True ele mostra
print(resp)