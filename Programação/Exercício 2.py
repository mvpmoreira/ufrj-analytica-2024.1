import numpy as np


colunas = 'abcdefgh'
linhas = '87654321'


while True:
    tabuleiro = np.zeros((8, 8))    
    ans = input("Faça uma jogada: ")
    ans = ans.casefold().strip()

    if ans == 'f':
        print('Fim...')
        break

    ans = ans.zfill(4)
    inicio = ans[:-2].strip()
    fim = ans[-2:]
    inicio_existe, fim_existe = True, True

    if not (inicio[0] in colunas and inicio[1] in linhas):
            inicio_existe = False
    if not (fim[0] in colunas and fim[1] in linhas):
            fim_existe = False

    if not (inicio_existe or fim_existe):
        print('As duas posições fornecidas não existem no tabuleiro. Tente novamente.')
        continue 
    elif not inicio_existe:
        print('A posição de início não existe no tabuleiro. Tente novamente.')
        continue
    elif not fim_existe:
        print('A posição do final não existe no tabuleiro. Tente novamente.')
        continue
    elif inicio == fim:
        print('O início e o fim da jogada são iguais. Tente novamente.')  
        continue


    coluna_inicio = colunas.index(inicio[0])
    linha_inicio = linhas.index(inicio[1])
    

    def checar_se_disponivel(i, j):
        if i in range(8) and j in range(8):
            tabuleiro[i][j] = 1


    checar_se_disponivel(linha_inicio + 1, coluna_inicio + 2)
    checar_se_disponivel(linha_inicio + 2, coluna_inicio + 1)
    checar_se_disponivel(linha_inicio + 2, coluna_inicio - 1)
    checar_se_disponivel(linha_inicio + 1, coluna_inicio - 2)
    checar_se_disponivel(linha_inicio - 1, coluna_inicio - 2)
    checar_se_disponivel(linha_inicio - 2, coluna_inicio - 1)
    checar_se_disponivel(linha_inicio - 2, coluna_inicio + 1)
    checar_se_disponivel(linha_inicio - 1, coluna_inicio + 2)

    coluna_fim = colunas.index(fim[0])
    linha_fim = linhas.index(fim[1])
    if tabuleiro[linha_fim][coluna_fim] == 1:
        print('O movimento é VÁLIDO.')
    else:
        print('O movimento é INVÁLIDO.')
