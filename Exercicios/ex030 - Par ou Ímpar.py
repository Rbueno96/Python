num = int(input('Por favor, me diga um número: '))
resultado = num % 2
if resultado == 0:
    print('O número escolhido foi {}, e este número é Par'.format(num))
else:
    print('O número escolhido foi {}, e este número é Ímpar'.format(num))
