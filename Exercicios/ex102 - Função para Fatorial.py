def fatorial(num=1, show=False):  #Aqui eu determino mais um parâmetro para receber dois lá quando chamar
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    def por Rodbueno
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            print(' x ' if c > 1 else (' = '), end='')
        f *= c
    return f


# Programa Principal
print(fatorial(6, show=True))  #Esse parâmetro vai mostrar o cálculo ou não
help(fatorial)