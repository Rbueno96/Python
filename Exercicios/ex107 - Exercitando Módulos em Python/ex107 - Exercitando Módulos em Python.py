import moeda
p = float(input('Digite o preço do produto: R$'))
print(f'A metade de {p} é igual à {moeda.metade(p)}')
print(f'O dobro de {p} é igual à {moeda.dobro(p)}')
print(f'Aumentando em 10% o valor de {p}, teremos {moeda.aumentar(p, 10):.2f}')
print(f'Descontando 13% do valor de {p}, teremos {moeda.diminuir(p, 13):.2f}')
