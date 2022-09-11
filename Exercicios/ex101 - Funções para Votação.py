"""from datetime import date
def voto(num):
    if num < 16:
        return 'Voto NEGADO'
    elif 16 <= num < 18:
        return 'Voto OPCIONAL'
    elif 18 <= num < 65:
        return 'Voto OBRIGATÓRIO'
    elif num >= 65:
        return 'Voto OPCIONAL'

ano = int(input('Digite o seu ano e nascimento: '))
idade = date.today().year - ano
print(f'Com {idade} anos: {voto(idade)}')"""

# RESOLUÇÃO DO GUANABARA
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# PROGRAMA PRINCIPAL
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
