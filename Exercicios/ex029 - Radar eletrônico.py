velocidade = int(input('À que velocidade você estava o veículo? '))
multa = (velocidade - 80) * 7
if velocidade >= 80:
    print('Você estava acima da velocidade permitida. Será multado em R${:.2f}'.format(multa))
else:
    print('Você estava dentro do limite de velocidade, à {}Km/h.'.format(velocidade))
print('Tenha atenção no trânsito. Drive safety!')