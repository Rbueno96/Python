from time import sleep
def linha():
    print('-' * 50)
def contador(i, f, p):
    if p < 0:
        p *= -1  #Aqui ele muda o valor de P para positivo para printar
        #print(f'Contagem de {i} até {f} de {p} em {p}')  não preciso desse print
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:  # Esse if precisa vir do lado de fora do for para caso o p seja negativo, seja alterado
        p *= -1  #Aqui ele muda novamente o valor de P para negativo para fazer o for
    for c in range(i, f+p, p):  # Somei f + p para que o último número seja o digitado
        print(f'{c}', end=', ')
        sleep(0.2)
    print('FIM!')
    linha()

contador(0, 10, 1)
contador(10, -1, -2)
sleep(10)
print('Vamos realizar uma contagem: ')
i = int(input('Qual é o primeiro número da contagem? '))
f = int(input('Qual é o último número da contagem? '))
p = int(input('De quantos em quantos números vamos contar? '))
contador(i, f, p)  # Não posso usar o print aqui na DEF pq se não ele vai trazer o valor NONE no final


#RESOLUÇÃO DO GUANABARA: GOSTEI MAIS DA MINHA
"""
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
            print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)"""
