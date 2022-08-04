#Para utilizar algumas funções específicas é necessário importar biblioteca ou módulos nesse caso.
#import 'tal biblioteca' -> Vai importar toda a biblioteca
#from 'tal biblioteca' import 'tal coisa' -> Importa alguma funcionalidade específica

"""import math #dessa forma eu preciso usar na função "math.sqrt"
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual à outro número {}'.format(num, raiz))"""

# Se eu importar somente a função, posso escrever direto sem o math. "sqrt"

"""import random

num = random.randint(1, 100)
print(num)"""

import emoji
print(emoji.emojize('Olá, Mundo! :earth_americas: :smile:', use_aliases=True))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))