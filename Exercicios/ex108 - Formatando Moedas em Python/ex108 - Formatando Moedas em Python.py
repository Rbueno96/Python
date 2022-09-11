import moeda
p = float(input('Digite o preço do produto: R$'))
print(f'A metade de {moeda.moeda(p)} é igual à {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é igual à {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando em 10% o valor de {moeda.moeda(p)}, teremos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Descontando 13% do valor de {moeda.moeda(p)}, teremos {moeda.moeda(moeda.diminuir(p, 13))}')
