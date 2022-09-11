def metade(preço = 0, format = False):
    resultado = preço / 2
    return resultado if format is False else moeda(resultado)


def dobro(preço = 0, format = False):
    resultado = preço * 2
    return resultado if format is False else moeda(resultado)


def aumentar(preço = 0, taxa = 0, format = False):
    resultado = preço + (preço * taxa / 100)
    return resultado if format is False else moeda(resultado)


def diminuir(preço = 0, taxa = 0, format = False):
    resultado = preço - (preço * taxa / 100)
    return resultado if format is False else moeda(resultado)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço}'.replace('.', ',')  #É possível substituir uma string por outra com replace


def resumo(preço = 0, acres = 0, desc = 0):
    aumento = aumentar(preço, acres, True)  #Analisei de forma com os parâmetros e apliquei
    redução = diminuir(preço, desc, True)
    print('-' * 30)
    print(f'{"Resumo do Valor":^30}')  #Poderia usar o método também .center(30), papai Guanabara escondendo o jogo dnv
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')  #\t significa tabulação e mantém ordenado e centralizado
    print(f'Dobro do Preço: \t{moeda(dobro(preço))}')  #Guanabara fica escondendo o jogo, nao ensina esses macetes
    print(f'Metade do Preço: \t{moeda(metade(preço))}')  #Mas da pra fazer dando o mesmo numero de espaços iguais
    print(f'{acres}% de aumento: \t{aumento}')  #Exemplo, aplicando 4x a barra de espaço em todos eles, ficaria alinhado
    print(f'{desc}% de redução: \t{redução}')
    print('-' * 30)
