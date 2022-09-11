from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)  #Aqui a gente coloca o índice da def para poder indicar dps com a função
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
def somapar(lista):
    soma = 0
    print()
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares é {soma}.')

numeros = list()
sorteia(numeros)
somapar(numeros)
