# Calcule o preço a pagar, sabendo que o carro custa R$60,0 por dia e R$0,15 km rodado

dias = int(input('Por quantos dias o carro ficou alugado? '))
km = int(input('Quantos km foram percorridos? '))
valor = (60 * dias) + (0.15 * km)
print('O valor à pagar será igual à {}'.format(valor))
