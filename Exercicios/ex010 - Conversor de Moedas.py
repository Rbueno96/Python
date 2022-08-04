real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.19
print('Com R${:.2f} você poderá comprar U${:.2f}'.format(real, dolar))
