# Equilátero - Lados iguais
# Isósceles - Dois lados iguais
# Escaleno - Todos os lados diferentes

print('=-='*20)
print('Vamos avaliar se três valores de retas podem formar um triângulo.')
print('=-='*20)
lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('Os segmentos podem formar um triângulo.')
    if lado1 == lado2 == lado3:
        print('Nesse caso, temos um triângulo EQUILÁTERO.')
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2:
        print('Nesse caso, temos um triângulo ISÓSCELES.')
    elif lado1 != lado2 != lado3:
        print('Nesse caso, temos um triângulo ESCALENO.')
else:
    print('Os segmentos não pode formar um triângulo.')
