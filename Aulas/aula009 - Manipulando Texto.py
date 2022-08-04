#FATIAMENTO de uma string:

"""frase = "Curso em video Python"
print(frase[0:21])
#O símbolo ":" indica o intervalo de strings que desejo adicionar.

print(frase[0:21:2])
#Esse último é indicador de skip, pular de 2 em 2 letras.

print(frase[:5])
#Não é necessário colocar o 0 na frente, ele inicia sempre no primeiro string.

print(frase[15:])
#Mesmo raciocínio do código acima, ele vai do 15 em diante até o final.

print(frase[9::3])
#Mesmo racicínio do código acima, não preciso colocar o número final caso eu não saiba. Nesse caso de 3 em 3.

#______________________________________________________________________________________________________________


#ANÁLISE de uma String:

#Para contar quantos caracteres possui a string:
print(len(frase))

#Para contar quantas vezes um caractere aparece numa string:
print('Existem', frase.count('o'), 'letras o nessa frase.')

#Para contar com fatiamento:
print('Existem', frase.count('o', 0, 13), 'no intervalo de 0 a 13.')

#Para encontrar uma sequencia de caracteres, mostrando em qual ponto da string se inicia:
print(frase.find('deo'))

#Quando procurar por uma palavra que não existe na string será retornado o valor de -1:
print(frase.find('Android'))

#Para retornar se algo está dentro da frase eu posso também utilizar o in, dessa forma retorna True or False:
print('Curso' in frase)

#______________________________________________________________________________________________________________

#TRANSFORMAÇÃO de uma string:

#Para substituir uma palavra dentro de uma string:
print(frase.replace('Python','Android'))

#Para efetivamente substituir a frase com a nova palavra eu devo atribuir novamente à variável:
frase = print(frase.replace('Python','Android'))

#Para transformar algum caractere minúsculo em maiúsculo:
print(frase.upper())

#Mesmo raciocínio acima. Para transformar em minúsculo:
print(frase.lower())

#Para capitalizar uma frase, isto é, transformar todas as letras em minúsculas e só a primeira letra maiúscula:
print(frase.capitalize())

#Para titularizar uma frase, isto é, transformar todas as primeiras letras de cada palavra maiúsculas:
print(frase.title())

#Para remover todos os espaços inúteis no início e no final da string:
print(frase.strip())
#Posso colocar o R de right antes do strip:
#Posso colocar o L de Left antes do strip:
print(frase.rstrip())
print(frase.lstrip())

#______________________________________________________________________________________________________________

#DIVISÃO de uma string:

#Para dividir o número de caracteres usamos o split. A frase tinha 21 caracteres, agora cada palavra terá sua divisão:
print(frase.split())

#JUNÇÃO de uma string:

#Para juntar as strings que foram divididas com o split, dentro das '' vai o que queremos colocar no lugar do espaço
'-'.join(frase)"""


#Aspas triplas podem ser usadas para comentar o código ou printar um texto inteiro de mais de uma linha


#PRÁTICA__________________________________________________________________________________________

frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido)
print(dividido[2])
print(dividido[2][3])