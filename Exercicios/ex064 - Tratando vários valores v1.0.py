n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número para somar [999 para interromper]: '))
    if n != 999:
        soma += n
        cont += 1
print('Foram digitados {} termos e a soma deles é igual à {}'.format(cont, soma))
