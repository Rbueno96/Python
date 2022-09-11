"""contador = produto = 0
print('-'*20)
numero = int(input('Quer ver a tabuada de qual valor? '))
print('-'*20)
while numero >= 0:
    if contador < 10:
        contador += 1
    else:
        break
    produto = numero * contador
    print(f'{numero} x {contador} = {produto}')
"""

"""numero = contador = produto = 0
numero = int(input('Digite um número para ver sua tabuada: '))
while True:
    if numero >= 0:
        if contador < 10:
            contador += 1
        else:
            break
        produto = numero * contador
        print(f'{numero} x {contador} = {produto}')
    elif numero < 0:
        break
print('-'*20)"""

numero = contador = produto = 0
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    contador = 0  # Ao invés de utilizar um contador basta eu colocar a variável C do for para multiplicar
    if numero < 0:
        break
    for c in range(1, 11):
        #if contador < 10:
         #   contador += 1 # NÃO PRECISO UTILIZAR O CONTADOR SÓ COLOCAR O C
        #produto = numero * contador
        print(f'{numero} x {c} = {numero * c}')
    print('-' * 20)
print('Programa encerrado. Volte sempre!')
