num = int(input('Vamos verificar se o número digitado é primo. Qual é o número? Digite: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
        print('O número {} é primo.'.format(num))
else:
        print('O número {} não é primo.'.format(num))
