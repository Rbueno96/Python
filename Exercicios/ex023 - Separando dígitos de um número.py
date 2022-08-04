num = int(input('Informe um número para análise entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade é {u}, a dezena é {d}, a centena é {c}, o milhar é {m}')