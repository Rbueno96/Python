l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
area = l * h
tinta = area / 2
print('A parede com dimensões de {}m x {}m, possui área total de {}m.\nEntão, será necessário {}L de tinta para pintá-la.'.format(l, h, area, tinta))
