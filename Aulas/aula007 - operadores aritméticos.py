# Um sinal de igual "=" representa uma atribuição "recebe". Enquanto dois sinais de igual "==" corresponde à "igual à
# quanto". 5 // 2 -> Divisão inteira -> 5 // 2 = 2 5 % 2 -> Resto da divisão -> 5 % 2 = 1

# 1° -> ( )
# 2° -> **
# 3° -> * / // %
# 4° -> + -
#Funcionalidades legais

"""
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome)) #alinhamento centralizado '^' com 20 '='
print('Prazer em te conhecer {:>20}!'.format(nome)) #alinhamento à direita '>'
print('Prazer em te conhecer {:<20}!'.format(nome)) #alinhamento à esquerda '<'
print('Prazer em te conhecer {:^20}!'.format(nome)) #alinhamento centralizado '^'
print('Prazer em te conhecer {:-^20}!'.format(nome)) #alinhamento centralizado '^' com 20 '-'
"""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n O produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ') # '\n' quebra uma linha
print('A divisão inteira é {}, e a potência é {}'.format(di, e)) # end='' insere qualquer coisa ou não permite a
# quebra de linha
print( )
print('A soma é {}, o produto é {}, e a divisão é {:.2f}'.format(s, m, d), end=' >>> ')
print('A divisão inteira é {}, e a potência é {}'.format(di, e))