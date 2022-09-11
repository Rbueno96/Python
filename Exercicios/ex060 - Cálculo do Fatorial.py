# POSSÍVEIS SOLUÇÕES

"""PRIMEIRAª
from math import factorial
n = int(input('Digite um número para cálculo do seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))"""

n = int(input('Digite um número para cálculo do seu fatorial: '))
c = n
f = 1.
print('Calculando {}! -> '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


"""n = int(input('Digite o número para cálculo do fatorial: '))
x = n - 1
while n != 0:
    fatorial = n * x
    print(fatorial, end='x')
    n -= 1
print('FIM')"""