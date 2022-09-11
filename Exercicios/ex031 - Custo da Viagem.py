dist = int(input('Qual é a distância em KM da sua viagem? '))
if dist <= 200:
    preço = (dist * 0.5)
else:
    preço = (dist * 0.45)
print('O preço da sua viagem será de R$ {:.2f}.'.format(preço))
