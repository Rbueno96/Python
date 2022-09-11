from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m,',  # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m',      # 6 - branco
     );                  # TUPLA DE CORES, só chamar a cor pelo número

# c[0] = '\033[0;30;41m'           Fiz isso apenas para mostrar que era uma tupla e é imutável
# print(c[0])

def ajuda(com):     #Função que define o comando help
    título(f'Acessando o manual do comando {com}', 4)  #O 4 é colocado para referenciar o background na cor desejada
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):  #Função que define o título
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * len(msg))
    print(f'  {msg}')
    print('~' * len(msg))
    print(c[0], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)