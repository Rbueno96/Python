"""lista = []  #Lista simples
lista.append('Rodrigo')  #Adicionamos um item a lista
lista.append(26)  #Outro item
print(lista)
print(lista[0])
print(lista[1])
pessoas = list()
# pessoas.append(lista[:])  # É uma cópia da lista de cima e vai colocar uma lista dentro da lista
lista.append('Gustavo')
lista.append(39)
lista.append('Marcia')
lista.append('60')
pessoas.append(lista[:])  # Aqui ele faz 2 cópias do RODRIGO, 26, pq já copiou em cima
print(pessoas)
# Colocar uma lista dentro de outra lista
segunda_lista = [['Rodrigo', 26], ['Maria', 19], ['Gustavo', 39]]  # [] representam listas né
print(segunda_lista[0][0])
print(segunda_lista[1])"""

#Parte prática da aula do Guanabara
"""teste = list()
teste.append('RODRIGO')
teste.append(26)
print(teste)
galera = list()
galera.append(teste[:])  # É imprescindível colocar o [:] para copiar a lista e não criar uma ligação entre elas
teste[0] = 'Maria'
teste[1] = 19  #Aqui estamos alterando a lista teste
print(teste)
galera.append(teste[:])  # No primeiro append foi adicionado o Rodrigo, dps mudado o teste e adicionado Maria
print(galera)
galera_dois = [['JOAO', 19], ['RODRIGO', 26], ['ANA', 21], ['MARIA', 45]]
print(galera_dois[1][0])
print(galera_dois[1])
for pessoa in galera_dois:
    print(pessoa)
    print(pessoa[0])
print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')"""
grupo = list()
dados = list()
maior = menor = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(int(input('Idade: ')))
    grupo.append(dados[:])
    dados.clear()  #É necessário apagar esses dados pq se não ficará adicionando sempre como 0 e 1 da cada lista
"""print(grupo)
print(dados)"""
print(grupo)
for pessoas in grupo:
    if pessoas[1] >= 21:
        print(f'{pessoas[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{pessoas[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maior de idade e {menor} menor de idade.')
