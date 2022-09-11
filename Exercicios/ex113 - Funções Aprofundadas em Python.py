cores = ('\033[31m',        #0 - vermelho
         '\033[m')          #1 - Sem cor

"""def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{cores[0]}Erro! Digite um número inteiro válido.{cores[1]}')
        if ok:
            break
    return valor


def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print(f'{cores[0]}Erro! Digite um número real válido.{cores[1]}')
        if ok:
            break
    return valor


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {n1} e {n2}')"""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores[0]}Erro: por favor, digite um número real válido.{cores[1]}')
            continue
        except KeyboardInterrupt:
            print(f'{cores[0]}Usuário preferiu não digitar esse número.{cores[1]}')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'{cores[0]}Erro: por favor, digite um número real válido.{cores[1]}')
            continue
        except KeyboardInterrupt:
            print(f'{cores[0]}Usuário preferiu não digitar esse número.{cores[1]}')
            return 0
        else:
            return n


num = leiaInt('Digite um valor inteiro: ')
num1 = leiaFloat('Digite um valor real: ')
print(f'Você digitou os números {num} e {num1}')