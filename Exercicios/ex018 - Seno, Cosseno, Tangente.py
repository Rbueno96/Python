import math
angulo = float(input('Digite o valor do angulo desejado: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} possui o seno de {:.2f}.'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} possui o Cosseno de {:.2f}.'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} possui a tangente de {:.2f}.'.format(angulo, tangente))
