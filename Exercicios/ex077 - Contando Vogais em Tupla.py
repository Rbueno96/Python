lista = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')  # O \n quebra a linha antes e o end não quebra dps
    for letra in palavra:
        if letra.lower() in 'aeiou':  #Daria pra pegar os acentos colocando eles dentro do in 'àáãâèéê e assim vai'
            print(letra, end=' ')

"""Lógica do programa bem simples... Para cada palavra na lista, printa aquilo ali, lembrando do upper para evitar 
qualquer problema. E depois para cada letra em palavra, já que palavras são uma lista de letras, pega cada letra, agora
com o lower, pra não ter problema e verifica se existe no aeiou. """