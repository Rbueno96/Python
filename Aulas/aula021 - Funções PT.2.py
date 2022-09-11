# Se eu quiser ver um manual de algum comando posso usar a função help()
# help(print)
# print(input.__doc__)
# DOCSTRING -> É uma documentação, ou manual, que ficará disponível ao criar uma função.
# O DOCSTRING é criado como comentário logo abaixo da def:

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Rodrigo Bueno assistir ao curso de Python.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
# help(contador)

# PARÂMETROS OPCIONAIS: Ao colocar o parâmetro igual à 0, ele se torna opcional.
def somar(a=0, b=0, c=0):
    """
    -> Realiza a soma de três, ou menos, valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    Função criada por Rodbueno no curso de Python.
    """
    soma = a + b + c
    print(f'A soma vale {soma}')
# Se eu quiser usar mais parâmetros, devo utilizar a técnica de descompactação '(*num)'

# somar(3, 2, 5)
# somar(3, 5)
# Posso também definir um parâmetro diretamente:
# somar(b=2, c=6) não preciso definir o a, e por definição ele é igual a 0.

# ESCOPO DE VARIÁVEIS
# Variável global é a que declaramos no programa principal e funcionará em todo o sistema. ESCOPO GLOBAL
# Variável local é o que declaramos apenas dentro de uma def e não será possível utilizar essa variável fora da def.
# ESCOPO GLOBAL ^

"""Vamos supor que eu tenha def teste(b):
E defina uma variável a = 5
ao chamar a função teste com parâmetro a, ou seja, teste(a)
o b passará a ter valor de a.

Vamos supor que a = 5
                def teste(b):
                    a = 8
                    b += 4
                    c = 2 
                    Nesse caso a de dentro da def, continuará valendo 8 e o B receberá o valor do A de fora
                    mais o seu valor de 4. B ficaria valendo A + B = 5 + 4 = 9
E os valores de dentro da def continuam sendo diferentes dos valores de fora para cada variável

Mas se eu colocar o 'GLOBAL A' dentro do def ele sempre mudará o valor global de a de 5 para 8."""

# RETORNO DE VALORES:
"""Ao utilizar o return vamos precisar definir uma variável para o resultado...
Não vamos utilizar o print e utilizar o return

EX: def somar(a=0, b=0, c=0):
        s = a + b + c
        return s
        
# PROGRAMA PRINCIPAL
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

Nesse caso eu posso formatar a resposta da forma como eu desejar:
print(f'Meus calculos deram {r1}, {r2} e {r3}"""

# PRÁTICA
def fatorial(num=1):  #Se não definir vale 1
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
"""        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='' )
    print(f'{f}')"""

n = int(input('Digite um número para ver seu fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}')

f1 = fatorial(6)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número para ver se é par ou ímpar: '))
if par(num):  #Essa def verifica apenas se o número é verdadeiramente par ou não. Então, se for True:
    print('É par!')
else:
    print('É ímpar!')
