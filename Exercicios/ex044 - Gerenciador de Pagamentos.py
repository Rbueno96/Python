print('{:=^36}'.format(' LOJAS BUENO ')) #O ^ indica centralizado e o 36 o número de espaços
total = float(input('Qual foi o valor total da compra? R$'))
opçao = int(input("""DENTRE AS FORMAS DE PAGAMENTO ABAIXO, ESCOLHA A OPÇÃO CORRESPONDENTE:
[ 1 ] - À VISTA DINHEIRO/CHEQUE;
[ 2 ] - À VISTA NO CARTÃO DE CRÉDITO;
[ 3 ] - EM ATÉ 2X SEM JUROS NO CARTÃO;
[ 4 ] - EM 3X OU MAIS NO CARTÃO COM JUROS.
SUA OPÇÃO É: """))
if opçao == 1:
    valor = total * 0.9
    print('A forma de pagamento escolhida foi À VISTA DINHEIRO/CHEQUE e o valor final é R${}'.format(valor))
elif opçao == 2:
    valor = total * 0.95
    print('A forma de pagamento escolhida foi À VISTA NO CARTÃO DE CRÉDITO e o valor final é R${}'.format(valor))
elif opçao == 3:
    valor = total
    print('A forma de pagamento escolhida foi EM ATÉ 2X SEM JUROS NO CARTÃO e o valor final é R${}'.format(valor))
elif opçao == 4:
    parcelas = int(input('Em quantas vezes quer dividir? '))
    valor = total * (1 + (parcelas * 0.2))
    print('A forma de pagamento escolhida foi EM {:.0f}X COM JUROS e o valor final é R${}'.format(parcelas, valor))
else:
    print('Você não digitou uma opção válida. Por favor, escolha novamente a opção correspondente à forma de pagamento')
