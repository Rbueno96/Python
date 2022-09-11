# Uma tupla é uma atribuição de mais de um valor para uma variável...

"""EXEMPLO: Se eu criar uma variável lanche = [hamburguer, suco, pizza, pudim] ; eu posso puxar no print um de cada vez
print(lanche[2]) -> Para puxar somente o terceiro elemento, pq o primeiro é 0.
print(lanche[0:2]) -> Ele vai mostrar do 0 até o 2, mas excluindo a pizza.
print(lanche[1:]) -> Vai do suco até o final.
print(lanche[-1]) -> De trás pra frente é o pudim.
len(lanche) -> Quantos elementos tem o lanche -> 4
for comida in lanche:
    print(c)  ->  Nesse caso vai printar todos os valores dentro de lanche e quando acabar vai encerrar o for

AS TUPLAS SÃO IMUTÁVEIS, não consigo alterar nenhum dos valores dentro de uma tupla durante a execução de um programa

USAMOS () -> TUPLAS
USAMOS [] -> LISTAS
USAMOS {} -> DICIONÁRIO

"""
"""
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:  #Para cada comida na tupla lanche
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(len(lanche))
print(lanche[-2], '\n')  # O numero que referencia o valor a ser exibido sempre vai em colchetes

# outra maneira de executar o for:

for cont in range(0, len(lanche)):
    print(lanche[cont])  # É preciso colocar o cont em função do lanche para que não seja mostrado o contador

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')  # Sempre que precisar mostrar a posição é assim

for posição, comida in enumerate(lanche):   # Com enumerate eu crio duas variáveis
    posição +=1  # preciso somar um para que o primeiro fique na posição 1
    print(f'Eu vou comer {comida} na posição {posição}.')

print(sorted(lanche))  # Coloca ordenado de forma alfabética"""

# QUANDO EU QUISER SOMAR TUPLAS, ELAS VÃO SE UNIR:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))  # contar algum valor
print(c.index(1))  # mostra a posição de algum valor
print(c.index(5, 1))  # o segundo valor mostra à partir daquela posição
