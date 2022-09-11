""" Para verificar as exceções vamos usar o
try: operação
except: falhou
else: deu certo
finally: certo/falha

"""

try:  #Tente fazer tal coisa
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

#PODEMOS TER VÁRIOS EXCEPTS DE ACORDO COM A NECESSIDADE DE TRATAMENTO DESSAS EXCEÇÕES
except Exception as erro:  #Se der erro, faça isso
    print(f'Problema encontrado foi {erro.__class__}')  #Aqui mostramos a classe do erro
    print(f'Problema encontrado foi {erro.__cause__}')
    print(f'Problema encontrado foi {erro.__context__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.1f}')  #Se der certo, faça isso
finally:
    print('Volte sempre, obrigado.')  #Independente se deu certo ou errado, faça isso

