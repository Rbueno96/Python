peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura **2)
print('O IMC dessa pessoa é de {}.'.format(imc))
if imc < 18.5:
    print('O seu imc é igual à {:.2f} e você está ABAIXO DO PESO!'.format(imc))
elif 18.5 <= imc < 25:
    print('O seu imc é igual à {:.2f} e você está no PESO IDEAL!'.format(imc))
elif 25 <= imc < 30:
    print('O seu imc é igual à {:.2f} e você está com SOBREPESO!'.format(imc))
elif 30 <= imc < 40:
    print('O seu imc é igual à {:.2f} e você está com OBESIDADE!'.format(imc))
elif imc >= 40:
    print('O seu imc é igual À {:.2f} e você está com OBESIDADE MÓRBIDA!'.format(imc))
