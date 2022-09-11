"""lista = list()
for numero in range(0, 5):
    valor = int(input('Digite um valor: '))
    if numero == 0:
        lista.append(valor)
    elif valor > lista[len(lista)-1]:
        lista.append(valor)
    print(f'Adicionado à posição {lista.find(valor)} da lista...')
print(lista)"""

# RESOLUÇÃO DO GUANABARA

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:  # Esse lista -1 é pra pegar o último elemento e comparar
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
