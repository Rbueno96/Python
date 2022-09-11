n = int(input('Digite um número inteiro para ver sua tabuada: '))
print('A TABUADA DE {} É: '.format(n))
for c in range(0, 11, 1):
    x = n * c
    print('{} X {} = {}'.format(n, c, x)) # eu poderia colocar no lugar da variavel x direto ( n * c )
