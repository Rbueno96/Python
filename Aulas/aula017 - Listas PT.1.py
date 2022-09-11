"""# As listas podem ser alteradas, são mutáveis.

lanche = ['hamburguer', 'suco', 'pizza', 'picolé']
print(lanche)

# ADICIONANDO ELEMENTOS:

# Para adicionar um elemento à uma lista eu utilizo o comando append:

lanche.append('bixcoito')
print(lanche)

# Para inserir um elemento em determinada posição eu utilizo o comando insert:

lanche.insert(0, 'cachorro-quente')
print(lanche)

# APAGANDO ELEMENTOS:

# Para apagar um elemento da lista utilizamos os seguintes comandos:

del lanche['indíce']  #Nesse caso eu indico o índice
lanche.pop('índice')  #Mais utilizado para apagar o último elemento, mas posso utilizar o índice
lanche.remove('elemento')  #Nesse caso eu indico o elemento, pelo seu nome, não o índice

lanche.pop(2)  #Removi o suco que passou a ser o elemento 2 por causa do cachorro-quente
print(lanche)

# CRIANDO LISTA COM UM RANGE:

valores = list(range(4, 20, 2))   #Aqui já é criado uma estrutura já crescente de forma ordenada
print(valores)

novos_valores = [1, 8, 5, 11, 12, 36, 10, 7, 4]
#Se eu precisar alinhar esses valores eu uso o sorted:
novos_valores.sort()  # Esse comando altera de vez a variável, ficando sempre em ordem crescente
print(novos_valores)
#Se eu precisar alinhar de forma decrescente utilizo o comando:
novos_valores.sort(reverse=True)  # Esse comando altera de vez a variável, ficando sempre em ordem decrescente
print(novos_valores)

# Para saber a quantidade de elementos numa lista eu utilizo:
print(len(novos_valores)+1)  #Lembrando que o +1 é pq o primeiro é considerado como 0"""

# =====================================================================================================================
# PRÁTICA
"""
num = [2, 5, 9, 1]
num[2] = 3  #Nesse caso o terceiro elemento [2] receberá uma substituição no seu valor, de 9 passará a ser 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)  # Inserir na posição 2, o número 0
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')"""

"""valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for numero in valores:
    print(f'{numero}...')

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')"""

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor qualquer: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

print(valores)

# Para copiar uma lista:
a = [2, 3, 4, 7]
b = a  #Nesse caso se eu alterar qualquer coisa em b, a também será alterado
b[2] = 8  #Nesse exemplo, o a também recebe 8

#Agora devo fazer o b receber todos os itens de a, mas sem alterar o A propriamente dito:
b = a[:]  #Lendo assim, B recebe todos os itens de A. ASSIM CRIAMOS UMA CÓPIA


