def area(l, c):
    s = l * c
    print(f'A área de um terreno {l}m x {c}m é de {s}m²')


print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
