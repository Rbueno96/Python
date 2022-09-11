numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
"""while True:  # Nesse caso daria errado toda vez que digitasse um número que não fosse entre 0 e 20
    valor = int(input('Digite um número entre 0 e 20: '))
    if valor > 20:
        valor = int(input('Essa opção não é válida. Digite um número entre 0 e 20: '))
    elif valor < 0:
        valor = int(input('Essa opção não é válida. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {numeros[valor]}.')"""

while True:  # Essa foi a melhor solução
    valor = int(input('Digite um número entre 0 e 20: '))
    if 0 <= valor <= 20:
        print(f'Você digitou o número {numeros[valor]}')
    else:
        print('Opção inválida. Tente novamente. ', end='')


# Resolução do Guanabara

"""while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    if 0 <= valor <= 20:
        break
    print('Tente novamente. ', end='')  # Esse end no final vai fazer com que esse print e o input estejam na msm linha
print(f'Você digitou o número {numeros[valor]}.')"""
