"""# FUNÇÕES SÃO ROTINAS
# DEF são definições de uma função
# TODAS as funções tem parenteses depois
def mostralinha():
    print('-' * 30)


# É necessário ter duas linhas vazias entre a DEF e o programa principal
mostralinha()
# É possível também criar uma def para um título ou qualquer coisa em texto


def titulo(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


titulo('    CURSO EM VIDEO      ')
titulo('O Rodrigo está aprendendo python!')
titulo('  AGORA VAI  ')"""

"""# Primeiro exemplo prático:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


def contador(* num):  # Dessa forma é criado uma TUPLA
    for valor in num:
        print(f'{valor} ', end='')
    print()
    print('FIM!')

def contador2(* num):   #O * significa que vários parâmetros serão passados
    tam = len(num)
    print(f'Recebi os valores {num} e são, ao todo, {tam} números')


# Programa Principal
soma(6, 5)
soma(9, 9)
soma(3, 12)
soma(b=7, a=3)  #Também posso definir a variável dentro do parâmetro.
# soma(3, 9, 5)  #Aqui não tenho variável dentro do parâmetro para o 3º valor.
# Podemos empacotar paramêtros

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)"""

# Trabalhando def com LISTAS:
valores = [7, 2, 5, 0, 4]
# No exemplo do Guanabara, vamos supor que precisamos dobrar esses valores...
# Como as listas já são variáveis compostas, podemos passar a lista diretamente no def.

def dobra(lst):
    pos = 0
    while pos < len(lst):  # A posição é menor pq é sempre 1 a menos que o tamanho. Se tem 5, é 0,1,2,3,4
        lst[pos] *= 2
        pos += 1
print(len(valores))  # O tamanho da lista é sempre +1 que a última posição
print(valores)
dobra(valores)
print(valores)

#Como naquele caso da soma de 3 elementos sem ter sido definido tais variáveis...
def soma(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos o somatório de {soma}')

soma(5, 2)
soma(2, 9, 4)
