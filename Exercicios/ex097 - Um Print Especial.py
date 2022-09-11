def escreva():
    print(f'{"-" * (len(texto) + 4):^{len(texto)}}')
    print(f'{texto:^{len(texto) + 4}}')
    print(f'{"-" * (len(texto) + 4):^{len(texto)}}')


texto = str(input('Digite um texto qualquer: ')).strip()
escreva()

#Poderia ter feito criando uma variável para o tamanho do texto

tam = len(texto) + 4  #Dessa forma eu só colocaria tam onde tem len(texto) + 4
#No caso meu programa está muito mais completo pois está também formatado ao centro e etc, guanabara não fez isso