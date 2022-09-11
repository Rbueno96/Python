tupla = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}.')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu em {tupla.index(3)+1}ª posição.')  # Tenho que ter o if pq se não for digitado 3 da erro
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')  # Esse end faz o print debaixo sair junto aqui
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end='; ')
