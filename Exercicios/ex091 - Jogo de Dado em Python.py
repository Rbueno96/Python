from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()  #Aqui ele virou uma lista
print('Valores sorteados:')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  #A chave nesse caso é o itemgetter de 1 para
#considerar os valores de randint. E o reverse=True é para pegar do maior para o menor.
# print(ranking)
for i, v in enumerate(ranking):  #Enumerate pq é uma lista
        print(f'{i+1}º lugar: {v[0]} com {v[1]}')  #Dentro é uma tupla, então v0 e v1 imutáveis
        sleep(1)
