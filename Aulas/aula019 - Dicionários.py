"""#Para criar um dicionário:
dados = dict()
dados = {'nome':'Pedro', 'idade':25}  #Já tinha visto isso com cores no terminal
print(dados['nome'])
print(dados['idade'])

#Para adicionar mais um elemento ao dicionário:
dados['sexo'] = 'M'

#Para eliminar um elemento:
del dados['idade']  #Aqui apagamos o idade
print(dados)

#Para mostrar na tela os valores ou os índices:
filme = {'titulo':'Star Wars',
         'ano':'1977',
         'diretor':'George Lucas'}
print(filme.values())  #Aqui eu printo os valores contidos na lista
print(filme.keys())  #Aqui eu printo os índices da lista
print(filme.items())  #Aqui eu printo o valor e o índice

for k, v in filme.items():
    print(f'O {k} é {v}')

#É possível também colocar os dicionários dentro de uma lista

filme = {'titulo':'Star Wars',
         'ano':'1977',
         'diretor':'George Lucas'}
locadora = []
locadora.append(filme[:])  #NÃO CONSEGUI REALIZAR A CÓPIA DE UM DICIONARIO
print(locadora)
filme.clear()
print(locadora)
filme = {'titulo':'Avengers',
         'ano':'2012',
         'diretor':'Joss Whedon'}

#FIQUEI COM DÚVIDA AQUI SOBRE COMO ADICIONAR O DICIONÁRIO NUMA LISTA"""

#PARTE PRÁTICA

"""pessoas = {'nome':'Rodrigo', 'sexo':'M', 'idade':26}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas['peso'] = 98.5
#Para um for simples:
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
#Para um for composto, igual enumerate:
for k, v in pessoas.items():
    print(f'O {k} é {v}.')
"""
"""brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['sigla'])"""

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  #É assim que eu faço a cópia de um dicionário e não com [:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')