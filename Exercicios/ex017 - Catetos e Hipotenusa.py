import math
from math import sqrt, pow
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor do cateto oposto é {}, do cateto adjacente é {} e a hipotenusa é {}'.format(co, ca, hi))


#"""math.sqrt(pow(co, 2)+(pow(ca, 2)))"""