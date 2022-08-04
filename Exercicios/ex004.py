valor = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(valor))
print(valor, 'É somente números?', valor.isnumeric())
print(valor, 'É somente letras?', valor.isalpha())
print(valor, 'É somente letras minúsculas?', valor.islower())
print(valor, 'É somente letras maiúsculas?', valor.isupper())
print(valor, 'É somente espaços?', valor.isspace())
print(valor, 'É um misto de letras e números?', valor.isalnum())
print(valor, 'Está capitalizado?', valor.istitle())


