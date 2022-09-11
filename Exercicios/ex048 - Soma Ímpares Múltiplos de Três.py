# Calcular a soma de todos os ímpares que são multiplos de 3 e que se encontram entre 1 e 500.
soma = 0
contador = 0
from time import sleep
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print('A soma de todos os valores solicitados é {}.'.format(soma))
print('A quantidade de valores solicitados foi {}.'.format(contador))

# O PRINT NÃO PODE ESTAR DENTRO DO IF PQ SE NÃO ELE VAI SE REPETIR

