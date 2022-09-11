"""lista = list()
for valores in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {valores}: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições {lista.index(max(lista))}.')
print(f'O menor valor digitado foi {min(lista)} nas posições {lista.index(min(lista))}.')"""

# _________________________________________________________________________________________________________________

# RESOLUÇÃO DO GUANABARA:

lista = []
maior = 0
menor = 0
for c in range(0, 5):  # Um laço para receber 5 valores
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))  #Recebe os valores com input e add com append
    if c == 0:  # muda os valores do maior e menor para serem iguais ao valor digitado na primeira posição
        maior = menor = lista[c]
    else:
        if lista[c] > maior:  # Muda os valores do maior se o novo valor foi maior
            maior = lista[c]
        elif lista[c] < menor:  # Mesma coisa do if de cima
            menor = lista[c]
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')  # End para evitar a quebra de linha
for i, v in enumerate(lista):  # i é o índice no valor v da lista
    if v == maior:  # Se o valor for o maior escrever o índice na tela
        print(f'{i}... ', end='')
print()  # Esse print é só para quebrar de linha
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:  # Mesma coisa, se o valor for o menor escrever o índice na tela
        print(f'{i}... ', end='')
print()  #Só pra quebrar a linha
