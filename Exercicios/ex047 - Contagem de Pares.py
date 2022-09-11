#Contagem de pares de 1 à 50:
from time import sleep
for c in range(0, 51, 2):
    print('\033[34m', c, '\033[m', end=',') #End= para ficar na horizontal e colocar algo entre eles
    sleep(0.3)
print('DONE!')