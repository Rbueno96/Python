frase = str(input('Digite uma frase para verificar se ela é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# outra forma sem utilizar o for -> inverso = junto[::-1]
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase {} é um palíndromo.'.format(frase))
else:
    print('A frase {} não é um palíndromo.'.format(frase))
print('O inverso de {} é {}.'.format(junto, inverso))