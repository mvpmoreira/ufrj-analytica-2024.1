lista = []
lista_unicos = []
print('Digite números inteiros:')
while True:
    ans = input()
    ans = ans.strip().casefold()
    neg = None

    if ans == 'f':
        break
    if ans[0] == '-':
        neg = True
        ans = ans[1:]
    if not ans.isdigit():
        print('Isso não é um número inteiro. Tente novamente.')
        continue

    
    ans = int(ans)
    if neg is True:
        ans = -ans

    if ans not in lista_unicos:
        lista_unicos.append(ans)
    lista.append(ans)

lista_unicos.sort()
for i in lista_unicos:
    num = lista.count(i)
    print(f'O número {i} apareceu {num} vez{"es" if num != 1 else ""}.')
print('Fim...')
