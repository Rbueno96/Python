continuar = ''
contagem = 0
media = 0
soma = 0
maior = 0
menor = 0
while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] '))
    contagem += 1
    soma += numero
    if contagem == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
media += soma/contagem
print('Fim do programa. Você digitou {} números e a média foi de {:.1f}.'.format(contagem, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
