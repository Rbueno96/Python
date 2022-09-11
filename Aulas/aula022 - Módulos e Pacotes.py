"""A ideia aqui é apenas criar um programa ou funções em arquivos separados e importar por meio do IMPORT"""
import uteis        # Todas as defs estão no arquivo uteis.py
#Programa Principal
num = int(input('Digite o número: '))
fat = uteis.fatorial(num)
print(f'O fatorial de um {num} é {uteis.fatorial(num)}')
print(f'O dobro do número {num} é {uteis.dobro(num)}')

# O pacote é uma pasta que contém vários módulos

