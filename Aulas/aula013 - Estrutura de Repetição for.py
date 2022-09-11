""" UM LAÇO É UM COMANDO QUE SERÁ REPETIDO VÁRIAS VEZES POR UM DETERMINADO INTERVALO:

laço c no intervalo (1, 10)
    passo
pega

for c in range(1, 10):
    passo
pega

laço c no intervalo (0, 3)
    passo
    pula
passo
pula

for c in range(0, 3):
    passo
    pula
passo
pega

POSSO COLOCAR UM IF DENTRO DE UM FOR

for c in range(0, 3):
    if moeda:
        pega
    passo
    pula
passo
pega
"""
"""
for c in range(1, 6): #Ele sempre executa uma vez a menos do que o limite: EXEMPLO 5x nesse caso = 6 - 1
    print('Oi')
print('{:=^35}'.format(' FIM ')) # A identação é importante pq se eu puxar o print pra dentro do for, vai ficar OI FIM OI FIM OI FIM ...

for x in range(6, 0, -1):
    print(x) #Nesse caso o -1 é a iteração, o que vai acontecer no laço.
print('{:=^35}'.format(' FIM '))

for y in range(0, 9, 2): #De 0 até 8 pulando de 2 em 2.
    print(y)
print('{:=^35}'.format(' FIM '))

# UM CONTADOR:

n = int(input('Digite um número qualquer e vamos contar de 0 até esse número: '))
for u in range(0, n+1):
    print(u)
print('{:=^35}'.format(' FIM '))"""

"""# INICIO DO CONTADOR, FINAL DO CONTADOR + 1, INTERVALO ENTRE OS NUMEROS CONTADOS:
i = int(input('Digite o número inicial: '))
f = int(input('Digite o número final: '))
p = int(input('Digite o passo, ou seja, de quantos em quantos vamos pular: '))
for c in range(i, f+1, p):
    print(c)
print('{:=^35}'.format(' FIM '))
"""

#SOMATÓRIO ENTRE N NÚMEROS:

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n # posso escrever s += n
print('O somatório de todos os valores digitados foi {}.'.format(s))
