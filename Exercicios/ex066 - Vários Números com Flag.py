numero = contador = soma = 0
while True:
    numero = int(input('Digite um número para somar: [999 para encerrar] '))
    if numero != 999:
        contador += 1
        soma += numero
    else:
        break
print(f'Foram inseridos {contador} números e a soma entre eles foi igual à {soma}.')
