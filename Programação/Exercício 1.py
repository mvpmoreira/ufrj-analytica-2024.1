while True:
    ans = input('Digite o horário: ')
    ans = ans.strip()
    ans = ans.replace(';', ':').replace(',', ':').replace('.', ':').replace('>', ':').replace('?', ':')
   
    if ans == 'f':
        print('Fim...')
        break
    elif not (len(ans) == 5 and ans[2] == ':'):
        print('Input inválido. Tente novamente.')
    elif not (ans[:2].isdigit() and ans[-2:].isdigit()):
        print('Input inválido. Tente novamente.')
    elif not (int(ans[:2]) in range(0, 24) and int(ans[-2:]) in range(0, 60)):
        print('Input inválido. Tente novamente.')
    else:
        h = int(ans[:2])
        min = int(ans[-2:])
        # angulo_h = (h % 12)*30 + min/2
        angulo_h = (h % 12)*30
        angulo_min = min*6
        dif = abs(angulo_min - angulo_h)
        if dif > 180:
            dif = 360 - dif
        print(f'O menor ângulo é de {dif}°.')
