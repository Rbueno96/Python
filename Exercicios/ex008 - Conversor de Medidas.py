print('Vamos criar um conversor de medidas em metro.')
medida = float(input('Digite um valor em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
print(f'O valor de {medida}m é equivalente à: \n{dm}dm\n{cm}cm\n{mm}mm\n{km}km\n{dam}dam.')
