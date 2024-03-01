notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]


while True:
    ans = input('Digite a quantia em reais: R$ ')
    ans = ans.strip()
    ans = ans.replace(',', '.').replace(':', '.')
    ans = ans.zfill(4)
    if '.' not in ans:
        ans += '.00'

    if ans[-3] != '.':
        print('Quantia não reconhecida. Tente novamente.')
    elif not (ans[-2:].isdigit() and ans[:-3].isdigit()):
        print('Quantia não reconhecida. Tente novamente.')
    else:
        break


ans = float(ans)
num_notas, num_moedas = [], []

for n in notas:
    _ = int(ans // n)
    num_notas.append(_)
    ans = ans % n

for m in moedas:
    _ = int(ans // m)
    num_moedas.append(_)
    ans = ans % m  

print()
print('NOTAS:')
for i, _ in enumerate(notas):
    print(f'{num_notas[i]} nota{"s" if num_notas[i] != 1 else ""} de R$ {notas[i]:.2f}.')        
print()
print('MOEDAS:')
for i, _ in enumerate(moedas):
    print(f'{num_moedas[i]} moeda{"s" if num_moedas[i] != 1 else ""} de R$ {moedas[i]:.2f}.')        
print()
