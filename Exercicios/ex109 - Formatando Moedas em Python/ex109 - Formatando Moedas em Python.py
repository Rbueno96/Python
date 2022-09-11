import moeda
p = float(input('Digite o preço do produto: R$'))
print(f'A metade de {moeda.moeda(p)} é igual à {moeda.metade(p, True)}')  #True é o segundo parâmetro
print(f'O dobro de {moeda.moeda(p)} é igual à {moeda.dobro(p, True)}')
print(f'Aumentando em 10% o valor de {moeda.moeda(p)}, teremos {moeda.aumentar(p, 10, True)}')
print(f'Descontando 13% do valor de {moeda.moeda(p)}, teremos {moeda.diminuir(p, 13, True)}')
