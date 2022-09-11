"""numeros = []
pares = []
impares = []
temporario = []
for c in range(0, 7):
    temporario.append(int(input(f'Digite o {c}º valor: ')))
    if temporario[c] % 2 == 0:
        pares.append(temporario[:])
    else:
        impares.append(temporario[:])
temporario.clear()
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores impares digitados foram: {sorted(impares)}')"""

num = [[], []]  #Duas listas dentro de uma lista
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados: {num[0]}')
print(f'Os valores ímpares digitados: {num[1]}')
