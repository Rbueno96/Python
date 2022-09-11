from time import sleep
opção = ''
soma = 0
multiplicação = 0
primeiro_valor = float(input('Primeiro valor: ')) # as variáveis precisam estar fora do while para nao se repetirem
segundo_valor = float(input('Segundo valor: '))
while opção != 5:
    sleep(1)
    opção = int(input("""[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
>>>>> Qual é a sua opção? """))
    print('Processando...')
    sleep(1)
    if opção == 1:
        soma = primeiro_valor + segundo_valor
        print('A soma entre {} + {} é {}.'.format(primeiro_valor, segundo_valor, soma))
    elif opção == 2:
        multiplicação = primeiro_valor * segundo_valor
        print('A multiplicação entre {} X {} é {}.'.format(primeiro_valor, segundo_valor, multiplicação))
    elif opção == 3:
        if primeiro_valor > segundo_valor:
            print('{} é maior que {}.'.format(primeiro_valor, segundo_valor))
        elif primeiro_valor == segundo_valor:
            print('{} é igual à {}.'.format(primeiro_valor, segundo_valor))
        elif primeiro_valor < segundo_valor:
            print('{} é maior que {}.'.format(segundo_valor, primeiro_valor))
    elif opção == 4:
        print('Informe novamente os números:')
        primeiro_valor = float(input('Primeiro valor: '))
        segundo_valor = float(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-='*15)

# RESOLUÇÃO DO GUANABARA