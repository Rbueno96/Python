nome = str(input('Qual é o seu nome? '))
if nome == 'Rodrigo':
    print('\033[34mQue nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José' or nome == 'Augusto':
    print('Você tem um nome bem comum no Brasil!')
else:
    print('Você tem um nome não tão comum e não tão bonito!')
print('Tenha um bom dia, \033[34m{}!'.format(nome))

#Posso usar quantos elif eu quiser.
#Não preciso utilizar o else.
