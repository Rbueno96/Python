times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
pesquisa = str(input('De qual time você quer saber a posição? ')).strip().capitalize()
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[:5]}')  # Do 0 até o 4º que é 5-1
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')  # -4 é o ultimo -4 até : que é o final
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')  #Sorted é pra colocar em ordem alfabética
print('-='*15)
print(f'O Chapecoense estava na {times.index("Chapecoense")+1}ª posição.')  #Index é para denotar um índice
print('O time {} estava na {}ª posição.'.format(pesquisa, times.index(pesquisa)+1))
print(f'O time {pesquisa} estava na  {times.index(pesquisa)+1}ª posição.')
