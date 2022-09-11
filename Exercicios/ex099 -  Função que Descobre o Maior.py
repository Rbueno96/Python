"""def maior(* num):
    from time import sleep
    numeros = []
    numeros.append(num)
    linha()
    if len(num) == 0:
        num = 0
    print('Analisando os valores passados...')
    for k, v in enumerate(numeros):
        print(f'{(num)} Foram informados {len(v)} valores ao todo')
    print(f'Maior valor informado foi {max(num)}.')  #Não consegui fazer o max num para quando não é inserido valor


maior(5, 2, 8, 6, 1, 3)
maior(3, 7, 1)
maior(6, 4)
maior(1)
maior()"""

# RESOLUÇÃO GUANABARA NÃO UTILIZARÁ LISTAS
from time import sleep
def linha():
    print('-=-' * 30)
def maior(* num):
    cont = maior = 0
    linha()
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)  #Esse flush é para não ter o problema de renderização
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')
    sleep(1)


maior(5, 2, 8, 6, 1, 3)
maior(3, 7, 1)
maior(6, 4)
maior(1)
maior()
