expressao = str(input('Digite a expressão: '))  # O comando string transforma a expressão em uma lista
pilha = []
for simbolo in expressao:  # Para cada item da lista, ou seja, letra da palavra
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

# ---------------------------------------------------------------------------------------------------------------------
