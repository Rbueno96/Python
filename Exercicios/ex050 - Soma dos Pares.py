soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor para somar: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números pares e a soma dos números é igual à {}.'.format(cont, soma))