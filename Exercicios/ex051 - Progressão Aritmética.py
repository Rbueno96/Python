print('{:=^48}'.format(' 10 TERMOS DE UMA PA '))
cont = 0
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro_termo + (10 - 1 ) * razao
for c in range(primeiro_termo, decimo + 1 , razao):
    print(c, end=' -> ')
print('ACABOU')