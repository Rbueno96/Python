from random import randint #comando randint para randomizar um numero inteiro
from time import sleep #comando sleep faz o computador esperar um tempo
escolha_computador = randint(0, 5)
escolha_usuario = int(input('Tente adivinhar o número que eu vou pensar de 0 até 5: '))
print('Processando...')
sleep(2)
print('Ainda estou em dúvida...')
sleep(1)
print('Haha! Pensei no número {}'.format(escolha_computador))
if escolha_usuario == escolha_computador:
    print('Parabens, você acertou!')
else:
    print('Erroooou! Você escolheu {} e eu escolhi {}'.format(escolha_usuario, escolha_computador))
