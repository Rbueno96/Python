from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        total_maior += 1
  #      print('A {}ª pessoa é maior de idade.'.format(pessoas))
    else:
        total_menor += 1
  #      print('A {}ª pessoa é menor de idade.'.format(pessoas))
print('Temos {} pessoas maior de idade e {} pessoas menor de idade.'.format(total_maior, total_menor))
